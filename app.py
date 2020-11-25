import os
import requests
import json
import base64
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'plant_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_home")
def get_home():
    return render_template("index.html")


@app.route("/get_plants")
def get_plants():
    return render_template("plants.html",
                           plants=mongo.db.plants.find())


@app.route("/add_plants")
def add_plants():
    return render_template("addplants.html",
                           collections=mongo.db.collections.find())


@app.route("/insert_plant", methods=["GET", "POST"])
def insert_plant():
    plant = {
        "common_name": request.form.get("common_name"),
        "collection_name": request.form.get("collection_name"),
        "family_common_name": request.form.get("family_common_name"),
        "genus": request.form.get("genus"),
        "family": request.form.get("family"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
        "image_url": request.form.get("image_url"),
        "created_by": session["user"]
        }
    mongo.db.plants.insert_one(plant)
    flash("Plant Successfully Added")
    return redirect(url_for("get_plants"))

    collections = mongo.db.collections.find().sort("collection_name", 1)
    return render_template("addplants.html", collections=collections)


@app.route('/edit_plant/<plant_id>')
def edit_plant(plant_id):
    the_plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    all_collections = mongo.db.collections.find()
    return render_template("editplants.html", plant=the_plant,
                            collections=all_collections)


@app.route('/update_plant/<plant_id>', methods=["POST"])
def update_plant(plant_id):
    plants = mongo.db.plants
    plants.update({"_id": ObjectId(plant_id)},
    {
        "common_name": request.form.get("common_name"),
        "collection_name": request.form.get("collection_name"),
        "family_common_name": request.form.get("family_common_name"),
        "genus": request.form.get("genus"),
        "family": request.form.get("family"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
        "image_url": request.form.get("image_url"),
        "created_by": session["user"]
    })
    flash("Plant Successfully Edited!")
    return redirect(url_for("get_plants"))


@app.route('/delete_plant/<plant_id>')
def delete_plant(plant_id):
    mongo.db.plants.remove({"_id": ObjectId(plant_id)})
    return redirect(url_for("get_plants"))


@app.route("/get_collections")
def get_collections():
    return render_template("collections.html",
                           collections=mongo.db.collections.find())


@app.route("/add_collections")
def add_collections():
    return render_template("addcollections.html",
                           collections=mongo.db.collections.find())


@app.route("/insert_collection", methods=["GET", "POST"])
def insert_collection():
    collection = {
        "collection_name": request.form.get("collection_name"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
        "created_by": session["user"]
        }
    mongo.db.collections.insert_one(collection)
    flash("Collection Successfully Added")
    return redirect(url_for("get_collections"))

    collections = mongo.db.collections.find().sort("collection_name", 1)
    return render_template("addcollections.html", collections=collections)


@app.route('/edit_collection/<collection_id>')
def edit_collection(collection_id):
    the_collection = mongo.db.collections.find_one(
        {"_id": ObjectId(collection_id)})
    all_collections = mongo.db.collections.find()
    return render_template("editcollections.html",
                           collection=the_collection,
                           collections=all_collections)


@app.route('/update_collection/<collection_id>', methods=["POST"])
def update_collection(collection_id):
    collections = mongo.db.collections
    collections.update({"_id": ObjectId(collection_id)},
    {
        "collection_name": request.form.get("collection_name"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
        "created_by": session["user"]
    })
    flash("Collection Successfully Edited!")
    return redirect(url_for("get_collections"))


@app.route('/delete_collection/<collection_id>')
def delete_collection(collection_id):
    mongo.db.collections.remove({"_id": ObjectId(collection_id)})
    return redirect(url_for("get_collections"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "phone_number": request.form.get("phone_number").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get(
                        "username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/get_users")
def get_users():
    return render_template("user_details_card.html",
                           users=mongo.db.users.find())


ENDPOINT = "https://trefle.io/api/v1/plants/search?"
ALLPLANTSENDPOINT = "https://trefle.io/api/v1/plants?"
HTTPS = "https://trefle.io"
ALLPLANTS = "/api/v1/plants?"
PLANTSEARCH = "/api/v1/plants/search?"
YOUR_TREFLE_TOKEN = os.environ.get("YOUR_TREFLE_TOKEN")
TOK = "token="
STRG = "&q="
SEARCH = "black"
SEARCH_SPECIES = "lily"
PAGE = "&page="
NUMBER = 2

ENDPOINT_SPECIES = "https://trefle.io/api/v1/species/search?"
FILTER = "&filter[common_name]=rose"

trefle = requests.get(
    f"{HTTPS}{PLANTSEARCH}{TOK}{YOUR_TREFLE_TOKEN}{STRG}{SEARCH}").json()
trefle_plants = trefle['data']
trefle_links = trefle['links']
trefle_total = trefle['meta']
trefle_first = trefle_links['first']
trefle_current = trefle_links['self']
trefle_next = trefle_links['next']
trefle_next_page = trefle_next[27:]
trefle_last = trefle_links['last']
trefle_last_page = trefle_last[27:]
trefle_end = requests.get(
    f"{HTTPS}{PLANTSEARCH}{TOK}{YOUR_TREFLE_TOKEN}{PAGE}{trefle_last_page}").json()
trefle_end_links = trefle_end['links']
trefle_prev = trefle_end_links['prev']
trefle_prev_page = trefle_prev[27:]
print(trefle_end_links)

species_filter = requests.get(
    f"{ENDPOINT_SPECIES}{TOK}{YOUR_TREFLE_TOKEN}{STRG}{SEARCH_SPECIES}")


searches = species_filter.json()

trefle_all = requests.get(
    f"{HTTPS}{ALLPLANTS}{TOK}{YOUR_TREFLE_TOKEN}").json()
NUMBER = NUMBER + 1
trefle_all = requests.get(
    f"{HTTPS}{ALLPLANTS}{TOK}{YOUR_TREFLE_TOKEN}").json()
# print(trefle_all['links'])

# @app.route("/search", methods=["GET", "POST"])
# def search():
#     query = request.form.get("query")
#     tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
#     return render_template("trefle_plants.html", tasks=tasks)


@app.route("/search_trefle", methods=["GET", "POST"])
def search_trefle():
    query = request.form.get("query")
    plants = requests.get(
    f"{HTTPS}{PLANTSEARCH}{TOK}{YOUR_TREFLE_TOKEN}{STRG}{query}").json()
    plant = plants['data']
    links = plants['links']
    selfs = links['self']
    first = links['first']
    current = links['self']
    last = links['last']
    meta = plants['meta']
    total = meta['total']
    if current != last and current == first:
        nexts = links['next']
        return render_template(
            "trefle_plants_first.html", plants=plant,
            self=selfs, first=first, nexts=nexts,
            current=current, last=last, total=total)
    if current != first and current != last:
        nexts = links['next']
        # prev = links['prev']
        return render_template(
            "trefle_plants_prev.html", plants=plant,
            selfs=selfs, first=first, nexts=nexts,
            current=current, last=last, total=total)
    if current != first and current == last:
        prev = links['prev']
        return render_template(
            "trefle_plants_last.html", plants=plant,
            selfs=selfs, first=first, prev=prev,
            current=current, total=total)
    return render_template(
            "trefle_plants.html", plants=plant,
            selfs=selfs, total=total)


@app.route("/get_trefle_many")
def get_trefle_many():
    plants = requests.get(
    f"{HTTPS}{ALLPLANTS}{TOK}{YOUR_TREFLE_TOKEN}").json()
    plant = plants['data']
    links = plants['links']
    first = links['first']
    current = links['self']
    last = links['last']
    meta = plants['meta']
    total = meta['total']
    if current != last and current == first:
        nexts = links['next']
        return render_template(
            "trefle_plants_first.html", plants=plant,
            first=first, nexts=nexts,
            current=current, last=last, total=total)
    if current != first and current != last:
        nexts = links['next']
        # prev = links['prev']
        return render_template(
            "trefle_plants_prev.html", plants=plant,
            first=first, nexts=nexts,
            current=current, last=last, total=total)
    if current != first and current == last:
        prev = links['prev']
        return render_template(
            "trefle_plants_last.html", plants=plant,
            first=first, prev=prev,
            current=current, total=total)
    return render_template(
            "trefle_plants.html", plants=plant,
            total=total)


@app.route("/get_trefle_next")
def get_trefle_next():
    plants = requests.get(f"{HTTPS}{PLANTSEARCH}{TOK}{YOUR_TREFLE_TOKEN}{PAGE}{trefle_next_page}").json()
    plant = plants["data"]
    links = plants['links']
    first = links['first']
    current = links['self']
    last = links['last']
    meta = plants['meta']
    total = meta['total']
    if current != first and current != last:
        prev = links['prev']
        nexts = links['next']
        return render_template(
            "trefle_plants_prev.html", plants=plant,
            first=first, prev=prev, nexts=nexts,
            current=current, last=last, total=total)
    return render_template(
            "trefle_plants_last.html", plants=plant,
            first=first, prev=prev,
            current=current, total=total)


@app.route("/get_trefle_prev")
def get_trefle_prev():
    plants = requests.get(f"{HTTPS}{PLANTSEARCH}{TOK}{YOUR_TREFLE_TOKEN}{PAGE}{trefle_prev_page}").json()
    plant = plants["data"]
    links = plants['links']
    first = links['first']
    current = links['self']
    last = links['last']
    meta = plants['meta']
    total = meta['total']
    if current != first and current != last:
        prev = links['prev']
        nexts = links['next']
        return render_template(
            "trefle_plants_prev.html", plants=plant,
            first=first, prev=prev, nexts=nexts,
            current=current, last=last, total=total)
    return render_template(
            "trefle_plants_first.html", plants=plant,
            last=last, nexts=next,
            current=current, total=total)


@app.route("/get_trefle_last")
def get_trefle_last():
    plants = requests.get(f"{HTTPS}{PLANTSEARCH}{TOK}{YOUR_TREFLE_TOKEN}{PAGE}{trefle_last_page}").json()
    plant = plants["data"]
    links = plants['links']
    first = links['first']
    current = links['self']
    last = links['last']
    meta = plants['meta']
    total = meta['total']
    if current != first and current == last:
        prev = links['prev']
        return render_template(
            "trefle_plants_last.html", plants=plant,
            first=first, prev=prev,
            current=current, last=last, total=total)
    return render_template(
            "trefle_plants_first.html", plants=plant,
            first=first,
            current=current, last=last, total=total)


@app.route("/get_plant_id")
def get_plant_id():
    # encode image to base64
    with open("static/images/daisy.jpg", "rb") as file:
        images = [base64.b64encode(file.read()).decode("ascii")]

    your_api_key = os.environ.get("your_api_key")
    json_data = {
        "images": images,
        "modifiers": ["similar_images"],
        "plant_details": ["common_names",
            "url", "wiki_description", "taxonomy"]
    }

    response = requests.post(
        "https://api.plant.id/v2/identify", json=json_data,
        headers={
            "Content-Type": "application/json",
            "Api-Key": your_api_key
                }).json()

    for suggestion in response["suggestions"]:
        print(suggestion["plant_name"])    # Taraxacum officinale
        print(suggestion["plant_details"]["common_names"])    # ["Dandelion"]
        print(suggestion["plant_details"]["url"])    # https://en.wikipedia.org/wiki/Taraxacum_officinale
        print(suggestion["similar_images"])
        plant_name = suggestion["plant_name"]
        plant_details = suggestion["plant_details"]["common_names"]
        url_plant_details = suggestion["plant_details"]["url"]
        similar_images = suggestion["similar_images"]

    return render_template("plant_id.html", response=response,
            plant_name=plant_name, plant_details=plant_details, url_plant_details=url_plant_details, similar_images=similar_images)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
