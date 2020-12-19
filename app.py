import os
import json
import requests
import base64
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Cloudinary settings using python code. Run before pycloudinary is used.
cloudinary.config(
  cloud_name=os.environ.get('cloud_name'),
  api_key=os.environ.get('api_key'),
  api_secret=os.environ.get('api_secret')
)

# MongoDb access
app.config["MONGO_DBNAME"] = 'plant_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.secret_key = os.environ.get("SECRET_KEY")
# Trefle API call details
YOUR_TREFLE_TOKEN = os.environ.get("YOUR_TREFLE_TOKEN")
headers = {'Authorization': 'Token ' + YOUR_TREFLE_TOKEN}
# Cloudinary API call details
cloudinary_cloud_name = os.environ.get('cloud_name')
cloudinary_api_key = os.environ.get('api_key')
cloudinary_api_secret = os.environ.get('api_secret')

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
    return render_template(
        "addplants.html", collections=mongo.db.collections.find(
            {"created_by": session["user"]}))


@app.route("/insert_plant", methods=["GET", "POST"])
def insert_plant():
    user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
    plant = {
        "trefle_id": request.form.get("trefle_id"),
        "common_name": request.form.get("common_name"),
        "collection_name": request.form.get("collection_name"),
        "family_common_name": request.form.get("family_common_name"),
        "scientific_name": request.form.get("scientific_name"),
        "family_name": request.form.get("family_name"),
        "genus": request.form.get("genus"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
        "image_url": request.form.get("image_url"),
        "created_by": session["user"],
        "users": user_id
        }
    mongo.db.plants.insert_one(plant)
    flash("Plant Successfully Added")
    return redirect(url_for("get_plants"))

    collections = mongo.db.collections.find(
        {"created_by": session["user"]}).sort("collection_name", 1)
    return render_template("addplants.html", collections=collections)


@app.route('/edit_plant/<plant_id>')
def edit_plant(plant_id):
    the_plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    all_collections = mongo.db.collections.find(
        {"created_by": session["user"]})
    return render_template(
        "editplants.html", plant=the_plant, collections=all_collections)


@app.route('/update_plant/<plant_id>', methods=["POST"])
def update_plant(plant_id):
    user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
    plants = mongo.db.plants
    plants.update({"_id": ObjectId(plant_id)},
    {
        "trefle_id": request.form.get("trefle_id"),
        "common_name": request.form.get("common_name"),
        "collection_name": request.form.get("collection_name"),
        "family_common_name": request.form.get("family_common_name"),
        "scientific_name": request.form.get("scientific_name"),
        "family": request.form.get("family"),
        "genus": request.form.get("genus"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
        "image_url": request.form.get("image_url"),
        "created_by": session["user"],
        "users": user_id
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
    user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
    collection = {
        "collection_name": request.form.get("collection_name"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
        "created_by": session["user"],
        "users": user_id
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
    all_collections = mongo.db.collections.find(
        {"created_by": session["user"]})
    return render_template("editcollections.html",
                           collection=the_collection,
                           collections=all_collections)


@app.route('/update_collection/<collection_id>', methods=["POST"])
def update_collection(collection_id):
    # grab the session user's username from db
    user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
    collections = mongo.db.collections
    collections.update({"_id": ObjectId(collection_id)},
    {
        "collection_name": request.form.get("collection_name"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
        "created_by": session["user"],
        "users": user_id
    })
    flash("Collection Successfully Edited!")
    return redirect(url_for("get_collections"))


@app.route('/delete_collection/<collection_id>')
def delete_collection(collection_id):
    mongo.db.collections.remove({"_id": ObjectId(collection_id)})
    return redirect(url_for("get_collections"))


def mongo_collections():
    collections = mongo.db.collections
    for collection in collections.find():
        print(collection['collection_name'], collection['users_id'])


# mongo_collections()


def mongo_users():
    users = mongo.db.users.find()
    for user in users:
        print(user['_id'], user['username'])


# mongo_users()


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


@app.route('/edit_user/<user_id>')
def edit_user(user_id):
    the_user = mongo.db.users.find_one(
        {"_id": ObjectId(user_id)})
    all_users = mongo.db.users.find()
    return render_template("edituser.html",
                           user=the_user,
                           users=all_users)


@app.route('/update_user/<user_id>', methods=["POST"])
def update_user(user_id):
    users = mongo.db.users
    users.update({"_id": ObjectId(user_id)}, {"$set": {
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
        "email": request.form.get("email"),
        "phone_number": request.form.get("phone_number"),
        "profile_image": request.form.get("profile_image")
        }
        })
    flash("User Successfully Edited!")
    return redirect(url_for("get_users"))


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    return redirect(url_for("logout"))


PLANTSEARCH = "/api/v1/species/search?"
FILTER1 = "&filter"
FILTERNOT = "&filter_not[common_name]=None"
RANGE1 = "&range"
FILTERCRITERIA1 = "[flower_color]="
FILTERSEARCH1 = "blue"
RANGECRITERIA1 = "[light]="
RANGESEARCH1 = ",9"
FILTER = "&filter[common_name]=rose"

HTTPS = "https://trefle.io"
ALLPLANTS = "/api/v1/species?"
ONESPECIES = "/api/v1/species/"
url_page_no = HTTPS + PLANTSEARCH
url_one_species = HTTPS + ONESPECIES
url_all_plants = HTTPS + ALLPLANTS
search = []
STRG = "&q="
page_url = "&page="


@app.route("/get_trefle_many")
def get_trefle_many():
    page = request.args.get('page', 1, type=int)
    plants = requests.get(
        url_all_plants + page_url + str(page), headers=headers).json()
    plant = plants['data']
    total = plants['meta']['total']
    links = plants['links']
    first_page = links['first'][21:]
    prev_page = 0
    selfs_page = links['self'][21:]
    last_page = links['last'][21:]
#    print(links)
    if 'next' in links:
        next_page = links['next'][21:]
#        print(next_page)
        return render_template(
            "trefle_plants_first.html", plants=plant,
            last_page=last_page, total=total, page=page,
            next_page=next_page, first_page=first_page,
            prev_page=prev_page, selfs_page=selfs_page)
    if 'prev' in links:
        prev_page = links['next'][21:]
        return render_template(
            "trefle_plants_first.html", plants=plant,
            last_page=last_page, total=total, page=page,
            prev_page=prev_page, first_page=first_page)
    return render_template(
            "trefle_plants.html", plants=plant,
            total=total)


@app.route("/search_trefle", methods=["GET", "POST"])
def search_trefle():
    query = request.form.get("query")
    global search
    search = STRG + str(query)
    page = request.args.get('page', 1, type=int)
    plants = requests.get(
        url_page_no + page_url + str(page) + search, headers=headers).json()
    plant = plants['data']
    total = plants['meta']['total']
    links = plants['links']
    adjust = len(search)
    first = links['first'][28:]
    first_many = len(first)
    first_net_adjust = first_many - adjust
    first_page = first[:first_net_adjust]
    prev_page = 0
    selfs = links['self'][28:]
    selfs_many = len(selfs)
    selfs_net_adjust = selfs_many - adjust
    selfs_page = selfs[:selfs_net_adjust]
    last = links['last'][28:]
    last_many = len(last)
    last_net_adjust = last_many - adjust
    last_page = last[:last_net_adjust]
    all_pages = list(range(int(first_page)+1, int(last_page)))
    print(first_page, prev_page, selfs_page, last_page)
    if 'next' in links:
        nexts = links['next'][28:]
        nexts_many = len(nexts)
        nexts_net_adjust = nexts_many - adjust
        next_page = nexts[:nexts_net_adjust]
#        print(first_no_pages, next_page, last_no_pages)
        return render_template(
            "trefle_plants_first.html", plants=plant,
            last_page=last_page, total=total,
            next_page=next_page, first_page=first_page,
            all_pages=all_pages, page=page,
            selfs_page=selfs_page, prev_page=prev_page)
#    print(json.dumps(links, indent=2))
#    print(next_page_no, query_adjust)
    return render_template(
            "trefle_plants_first.html", plants=plant,
            total=total)


# trefle_pages()


@app.route("/next_url")
# @app.route("/search_trefle")
def next_url():
    page = request.args.get('page', type=int)
    plants = requests.get(
        url_page_no + page_url + str(page) + search, headers=headers).json()
    plant = plants['data']
    total = plants['meta']['total']
    links = plants['links']
    adjust = len(search)
    first = links['first'][28:]
    first_many = len(first)
    first_net_adjust = first_many - adjust
    first_page = first[:first_net_adjust]
    selfs = links['self'][28:]
    selfs_many = len(selfs)
    selfs_net_adjust = selfs_many - adjust
    selfs_page = selfs[:selfs_net_adjust]
    last = links['last'][28:]
    last_many = len(last)
    last_net_adjust = last_many - adjust
    last_page = last[:last_net_adjust]
    all_pages = list(range(int(first_page)+1, int(last_page)))
    print(selfs_page, page)
    if 'next' in links:
        nexts = links['next'][28:]
        nexts_many = len(nexts)
        nexts_net_adjust = nexts_many - adjust
        next_page = nexts[:nexts_net_adjust]
#        print(next_page)
        return render_template(
            "trefle_plants_first.html", plants=plant,
            last_page=last_page, total=total,
            next_page=next_page, first_page=first_page,
            all_pages=all_pages, page=page,
            selfs_page=selfs_page)
    return render_template(
            "trefle_plants.html", plants=plant,
            total=total)


# next_url()


@app.route("/add_trefle_plant/<id>", methods=["GET", "POST"])
def add_trefle_plant(id):
    the_plant = requests.get(
        url_one_species + id, headers=headers).json()
    all_collections = mongo.db.collections.find(
        {"created_by": session["user"]})
#    print(json.dumps(the_plant, indent=2))
#    print(json.dumps(the_plant['data'], indent=2))
    trefle_id = the_plant['data']['id']
    common_name = the_plant['data']['common_name']
    scientific_name = the_plant['data']['scientific_name']
    family_name = the_plant['data']['family']
    family_common_name = the_plant['data']['family_common_name']
    genus = the_plant['data']['genus']
    image_url = the_plant['data']['image_url']
#    for id in the_plant['data']:
#        print(id)
    flower = the_plant['data']['flower']
    foliage = the_plant['data']['foliage']
    fruit_or_seed = the_plant['data']['fruit_or_seed']
    specifications = the_plant['data']['specifications']
    growth = the_plant['data']['growth']
    bloom_months = growth['bloom_months']
    for deets in growth:
        print(deets)
    print(json.dumps(flower, indent=2))
    print(json.dumps(foliage, indent=2))
    print(json.dumps(fruit_or_seed, indent=2))
    print(json.dumps(specifications, indent=2))
    print(json.dumps(growth, indent=2))
    print(json.dumps(bloom_months, indent=2))
    return render_template(
        "add_trefle_plant.html", plant=the_plant,
        common_name=common_name, collections=all_collections,
        scientific_name=scientific_name, genus=genus,
        family_common_name=family_common_name,
        image_url=image_url, family_name=family_name,
        trefle_id=trefle_id)


@app.route("/get_plant_id")
def get_plant_id():
    # encode image to base64

    with open("static/images/lilium.jpg", "rb") as file:
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

    # print(response['suggestions'])
    for suggestion in response['suggestions']:
#        print(suggestion["plant_name"])
#        print(suggestion["plant_details"]["common_names"])
        # https://en.wikipedia.org/wiki/Taraxacum_officinale
#        print(suggestion["plant_details"]["url"])
#        print(suggestion["similar_images"])
        plant_name = suggestion["plant_name"]
        plant_details = suggestion["plant_details"]["common_names"]
        url_plant_details = suggestion["plant_details"]["url"]
        similar_images = suggestion["similar_images"]
        for similar in similar_images:
            url = similar['url']
            print(json.dumps(url, indent=2))

    return render_template(
            "plant_id.html", response=response, plant_name=plant_name,
            plant_details=plant_details,
            url_plant_details=url_plant_details,
            similar_images=similar_images, url=url)


@app.route("/upload_cloudinary_images")
def upload_cloudinary_images():
    cloudinary.uploader.upload("", width=200, height=400,
                               crop="fill", gravity="face")


# upload_cloudinary_images()


@app.route("/cloudinary_images")
def cloudinary_images():
    data = cloudinary.Search()\
        .expression('mygardenmanager')\
        .max_results('30')\
        .with_field('tags')\
        .execute()
    images = data["resources"]
#     print(json.dumps(data, indent=2))
    return render_template(
        "my_images.html", data=data,
        images=images)

# cloudinary_images()


@app.route("/cloudinary_search")
def cloudinary_search():
    data = cloudinary.Search()\
        .expression('folder:mygardenmanager')\
        .max_results('30')\
        .with_field('tags')\
        .execute()
    images = data["resources"]
    print(json.dumps(images, indent=2))
#    print(url)
#    with open(url, "rb") as file:
#        txt_image = [base64.b64encode(file.read()).decode("ascii")]
#        print(txt_image)


# cloudinary_search()


@app.route("/cloudinary_resources")
def cloudinary_resources():
    data = cloudinary.api.resources(
        max_results='100',
        resource_type='image',
        type='upload',
        prefix='mygardenmanager/')
    images = data["resources"]
    print(json.dumps(images, indent=2))
#    return render_template(
#        "my_images.html", data=data, images=images)


# cloudinary_resources()


@app.route("/cloudinary_update")
def cloudinary_update():
    data = cloudinary.api.update(
        'mygardenmanager/water plant',
        tags='water lily')
    print(json.dumps(data, indent=2))


# cloudinary_update()


@app.route("/cloudinary_rename")
def cloudinary_rename():
    cloudinary.uploader.rename(
        'mygardenmanager/vvshquurn8x9bqlmfibr',
        'mygardenmanager/Contemplation')
#    print(json.dumps(data, indent=2))


# cloudinary_rename()


@app.route("/cloudinary_delete")
def cloudinary_delete():
    data = cloudinary.api.delete_resources('')
    print(json.dumps(data, indent=2))


# cloudinary_delete()


@app.route("/cloudinary_destroy")
def cloudinary_destroy():
    cloudinary.uploader.destroy('mygardenmanager/Daisy')
#    print(result)
    return redirect(url_for(
        "cloudinary_images"))


# cloudinary_destroy()


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
