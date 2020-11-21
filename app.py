import os
import requests
import json
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
    return render_template("user_details.html",
                           users=mongo.db.users.find())


ENDPOINT = "https://trefle.io/api/v1/plants/search?"
HTTPS = "https://trefle.io"
YOUR_TREFLE_TOKEN = os.environ.get("YOUR_TREFLE_TOKEN")
TOK = "token="
STRG = "&q="
SEARCH = "rose of sharon"
SEARCH_SPECIES = "lily"
PAGE = "&page="
NUMBER = 1

# NEXTNUMBER = NUMBER + 1


ENDPOINT_SPECIES = "https://trefle.io/api/v1/species/search?"
FILTER = "&filter[common_name]=rose"


species_filter = requests.get(
    f"{ENDPOINT_SPECIES}{TOK}{YOUR_TREFLE_TOKEN}{STRG}{SEARCH_SPECIES}")


searches = species_filter.json()
# plants = searches['data']
# print(searches)
# print(searches['meta'])

#for item in plants:
#    link = item
#    print(link)


# print(len(plants['data']))

# print(type(plants['data']))
# plants = requests.get(
#    f"{ENDPOINT}{YOUR_TREFLE_TOKEN}{STRG}{SEARCH}{PAGE}{NUM}").json()

# for plant in plants['data']:
#    plant_id = plant['id']
#    name = plant['common_name']
#    family = plant['family']
#    family_common_name = plant['family_common_name']
#    image = plant['image_url']
#    links = plant['links']
#    print(f"Plant ID: {plant_id}\tName: {name}\tFamily:{family}\tFamily Common Name:{family_common_name}\tImage: {image}\n")

# print(species_filter)
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("trefle_plants.html", tasks=tasks)


@app.route("/get_trefle")
def get_trefle():
    plants = requests.get(
    f"{ENDPOINT}{TOK}{YOUR_TREFLE_TOKEN}{PAGE}{NUMBER}{STRG}{SEARCH}").json()
    plant = plants["data"]
    links = plants['links']
    first = links['first']
    current = links['self']
    last = links['last']
    meta = plants['meta']
    total = meta['total']
    # prev = links['prev']
    # nexts = links['next']
    return render_template(
        "trefle_plants.html", plants=plant,
        first=first, current=current, last=last, total=total)


@app.route("/get_trefle_many")
def get_trefle_many():
    plants = requests.get(
    f"{ENDPOINT}{TOK}{YOUR_TREFLE_TOKEN}{PAGE}{NUMBER}{STRG}{SEARCH}").json()
    plant = plants["data"]
    links = plants['links']
    first = links['first']
    current = links['self']
    last = links['last']
    meta = plants['meta']
    total = meta['total']
    if current != last:
        prev = links['prev']
        nexts = links['next']
        return render_template(
            "trefle_plants_many.html", plants=plant,
            first=first, prev=prev, nexts=nexts,
            current=current, last=last, total=total)
    return render_template(
            "trefle_plants.html", plants=plant,
            first=first, current=current,
            last=last, total=total)


NUM = 1
data = requests.get(f"{ENDPOINT}{TOK}{YOUR_TREFLE_TOKEN}{PAGE}{NUM}{STRG}{SEARCH}").json()
plants = data["data"]
pages = data['links']
current = pages['self']
last = pages['last']
total = data['meta']
print(pages, current, last, total)
if current != last:
    nexts = pages['next']
    newnext = nexts[27:]
    newlast = last[27:]
    NUM = NUM + 1
    data = requests.get(f"{ENDPOINT}{TOK}{YOUR_TREFLE_TOKEN}{PAGE}{newnext}").json()
    print(newlast, newnext)
else:
    if current == last:
        print("This are no more pages!")

# for page in range(2, data["total_pages"]+1):
#    discover_api = requests.get(discover_api_url + f"&page={page}").json()
#    most_popular_films.extend(discover_api["results"])

#printing movie_id and movie_title by popularity desc
# for i, film in enumerate(most_popular_films):
#    print(i, film['id'], film['title'])


# plant = plants['data']
# first = links['first']
# prev = links['prev']
# nexts = links['next']
# print(links['next'], nexts)
#   meta = plants['meta']
#   total = meta['total']
#   print(f"{first}\n{prev}\n{current}\n{nexts}\n{last}\n{total}")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
