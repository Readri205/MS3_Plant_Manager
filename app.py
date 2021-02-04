import os
# import json
import requests
import base64
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)
from werkzeug.utils import secure_filename
from PIL import Image
from shamrock import Shamrock


if os.path.exists("env.py"):
    import env

app = Flask(__name__)


# MongoDb access
app.config["MONGO_DBNAME"] = 'plant_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
# Secret Key Heroku
app.secret_key = os.environ.get("SECRET_KEY")
# paths to load images
app.config["IMAGE_UPLOADS"] = os.getenv('IMAGE_UPLOADS')
app.config["IMAGE_DEETS"] = os.getenv('IMAGE_DEETS')
# Trefle API call details
YOUR_TREFLE_TOKEN = os.environ.get("YOUR_TREFLE_TOKEN")
headers = {'Authorization': 'Token ' + YOUR_TREFLE_TOKEN}
# Shamrock python library for Trefle
api = Shamrock(YOUR_TREFLE_TOKEN)

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_home")
def get_home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


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
    collection_name = request.form.get("collection_name")
    collection_id = mongo.db.collections.find_one(
        {"collection_name": collection_name})['_id']
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
        "users": user_id,
        "collection_id": collection_id
    }
    mongo.db.plants.insert_one(plant)
    flash("Plant Successfully Added")
    return redirect(url_for("get_plants"))

    collections = mongo.db.collections.find(
        {"created_by": session["user"]}).sort("collection_name", 1)
    return render_template(
        "addplants.html", collections=collections)


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
    collection_name = request.form.get("collection_name")
    collection_id = mongo.db.collections.find_one(
        {"collection_name": collection_name})['_id']
    plants.update({"_id": ObjectId(plant_id)},
        {
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
            "users": user_id,
            "collection_id": collection_id
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
                           collections=mongo.db.collections.find(),
                           plants=mongo.db.plants.find())


@app.route("/collections_plants/<collection_id>")
def collections_plants(collection_id):
    the_collection = mongo.db.collections.find_one(
        {"_id": ObjectId(collection_id)})
    the_plants = mongo.db.plants.find()
    return render_template("collections_plants.html",
                           collection=the_collection,
                           collections=mongo.db.collections.find(),
                           plants=the_plants)


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


# Trefle Search & Filter API
# Global variables for Trefle API Search & Filters
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
next_page = []
prev_page = []
color_filter = []
STRG = "&q="
page_url = "&page="
filter_not = "filter_not"
pre = "%5B"
after = "%5D="


@app.route("/get_trefle_many")
def get_trefle_many():
    page = request.args.get('page', 1, type=int)
    plants = requests.get(
        url_all_plants + page_url + str(page), headers=headers).json()
    if plants:
        plant = plants['data']
        total = plants['meta']['total']
        return render_template(
                "trefle_search.html", plants=plant,
                total=total)
    else:
        return render_template(
                "trefle_oops.html")


@app.route("/search_trefle", methods=["POST"])
def search_trefle():
    if request.method == "POST":
        query = request.form.get("query")
        query = query.replace("'", "")
        query = query.replace(".", "")
        query = query.replace("-", "")
        query = query.replace("1", "")
    #    print(query)
        global search
        search = STRG + str(query)
    #    print(search)
        page = request.args.get('page', 1, type=int)
        plants = requests.get(
            url_page_no + page_url + str(page) + search, headers=headers).json()
        if plants:
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
            selfs_page = int(selfs[:selfs_net_adjust])
    #        print(selfs_page)
    #        prev_page = 0
            prev_page = selfs_page - 1
    #        print(prev_page)
    #        next_page = 2
            next_page = selfs_page + 1
            last = links['last'][28:]
            last_many = len(last)
            last_net_adjust = last_many - adjust
            last_page = last[:last_net_adjust]
    #        all_pages = list(range(int(first_page), int(last_page)+1))
            if int(last_page) == 3:
                return render_template(
                    "trefle_plants_three.html", plants=plant,
                    last_page=last_page, total=total,
                    next_page=next_page, first_page=first_page,
                    page=page, prev_page=prev_page,
                    selfs_page=selfs_page)
            if int(last_page) <= 2:
                return render_template(
                    "trefle_plants_two.html", plants=plant,
                    last_page=last_page, total=total,
                    next_page=next_page, first_page=first_page,
                    page=page, prev_page=prev_page,
                    selfs_page=selfs_page)
            return render_template(
                "trefle_plants.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                page=page, prev_page=prev_page,
                selfs_page=selfs_page)
        else:
            return render_template(
                        "trefle_oops.html")


@app.route("/next_url")
def next_url():
    page = request.args.get('page', type=int)
    plants = requests.get(
        url_page_no + page_url + str(page) + search, headers=headers).json()
    if plants:
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
        next_page = int(selfs_page) + 1
        prev_page = int(selfs_page) - 1
        last = links['last'][28:]
        last_many = len(last)
        last_net_adjust = last_many - adjust
        last_page = last[:last_net_adjust]
        all_pages = list(range(int(first_page), int(last_page)+1))
        if int(last_page) == 3:
            return render_template(
                "trefle_plants_three.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                all_pages=all_pages, page=page,
                prev_page=prev_page, selfs_page=selfs_page)
        if int(last_page) <= 2:
            return render_template(
                "trefle_plants_two.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                all_pages=all_pages, page=page,
                prev_page=prev_page, selfs_page=selfs_page)
        if int(last_page) == int(next_page):
            return render_template(
                "trefle_plants_last.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                all_pages=all_pages, page=page,
                prev_page=prev_page, selfs_page=selfs_page)
        if int(selfs_page) == int(first_page):
            return render_template(
                "trefle_plants_first.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                all_pages=all_pages, page=page,
                prev_page=prev_page, selfs_page=selfs_page)
        print(selfs_page)
        return render_template(
            "trefle_plants.html", plants=plant,
            last_page=last_page, total=total,
            next_page=next_page, first_page=first_page,
            all_pages=all_pages, page=page,
            prev_page=prev_page, selfs_page=selfs_page)
    else:
        return render_template(
                "trefle_oops.html")


@app.route("/add_trefle_plant/<id>", methods=["GET", "POST"])
def add_trefle_plant(id):
    the_plant = api.species(id)
    if the_plant:
        all_collections = mongo.db.collections.find(
            {"created_by": session["user"]})
        trefle_id = the_plant['data']['id']
        common_name = the_plant['data']['common_name']
        scientific_name = the_plant['data']['scientific_name']
        family_name = the_plant['data']['family']
        family_common_name = the_plant['data']['family_common_name']
        genus = the_plant['data']['genus']
        image_url = the_plant['data']['image_url']
        return render_template(
            "add_trefle_plant.html", plant=the_plant,
            common_name=common_name, collections=all_collections,
            scientific_name=scientific_name, genus=genus,
            family_common_name=family_common_name,
            image_url=image_url, family_name=family_name,
            trefle_id=trefle_id)
    else:
        return render_template(
                "trefle_oops.html")


@app.route("/get_trefle_deets/<id>", methods=["GET"])
def get_trefle_deets(id):
    the_plant = api.species(id)
    if the_plant:
        trefle_id = the_plant['data']['id']
        common_name = the_plant['data']['common_name']
        scientific_name = the_plant['data']['scientific_name']
        family_name = the_plant['data']['family']
        family_common_name = the_plant['data']['family_common_name']
        genus = the_plant['data']['genus']
        image_url = the_plant['data']['image_url']
        flower = the_plant['data']['flower']
        color = flower['color']
        conspicuous = flower['conspicuous']
        foliage = the_plant['data']['foliage']
        fruit_or_seed = the_plant['data']['fruit_or_seed']
        specifications = the_plant['data']['specifications']
        growth = the_plant['data']['growth']
        bloom_months = growth['bloom_months']
        return render_template(
            "plant_deets.html", plant=the_plant,
            common_name=common_name, flower=flower,
            scientific_name=scientific_name, genus=genus,
            family_common_name=family_common_name,
            image_url=image_url, family_name=family_name,
            trefle_id=trefle_id, foliage=foliage,
            fruit_or_seed=fruit_or_seed,
            color=color, conspicuous=conspicuous,
            specifications=specifications,
            bloom_months=bloom_months, growth=growth)
    return render_template(
        "trefle_oops.html")


@app.route("/filter_search")
def filter_search():
    return render_template("filter_trefle.html")


@app.route("/trefle_filter", methods=["GET", "POST"])
def trefle_filter():
    colors = []
    if request.method == "POST":
        if request.form.get('White') == 'on':
            colors.append('white,')
        if request.form.get('Red') == 'on':
            colors.append('red,')
        if request.form.get('Yellow') == 'on':
            colors.append('yellow,')
        if request.form.get('Blue') == 'on':
            colors.append('blue,')
        if request.form.get('Black') == 'on':
            colors.append('black,')
        if request.form.get('Orange') == 'on':
            colors.append('orange,')
        if request.form.get('Green') == 'on':
            colors.append('green,')
        if request.form.get('Brown') == 'on':
            colors.append('brown,')
        if request.form.get('Purple') == 'on':
            colors.append('purple,')
        include = "filter"
        filters = "flower_color"
        global color_filter
        color_filter = ''.join(colors)
        page = request.args.get(
            'page', 1, type=int)
        params = include + pre + filters + after + color_filter + "&" + str(page)
        plants = requests.get(
            url_all_plants, params=params,
            headers=headers).json()
        if plants:
            plant = plants['data']
            total = plants['meta']['total']
            links = plants['links']
            selfs = links['self']
#            global adjust_page
            adjust_page = len(selfs) + 6
            first_page = links['first'][int(adjust_page):]
            selfs_page = page
            prev_page = page - 1
            next_page = page + 1
            last_page = links['last'][int(adjust_page):]
#            all_pages = list(range(int(first_page), int(last_page)+1))
            print(selfs_page, first_page, next_page, last_page, prev_page)
            if int(last_page) == 3:
                return render_template(
                    "filter_plants_three.html", plants=plant,
                    last_page=last_page, total=total,
                    next_page=next_page, first_page=first_page,
                    page=page,
                    prev_page=prev_page, selfs_page=selfs_page)
            if int(last_page) == 2:
                return render_template(
                    "filter_plants_two.html", plants=plant,
                    last_page=last_page, total=total,
                    next_page=next_page, first_page=first_page,
                    page=page,
                    prev_page=prev_page, selfs_page=selfs_page)
            if int(last_page) == int(next_page):
                return render_template(
                    "filter_plants_last.html", plants=plant,
                    last_page=last_page, total=total,
                    next_page=next_page, first_page=first_page,
                    page=page,
                    prev_page=prev_page, selfs_page=selfs_page)
            else:
                return render_template(
                    "filter_plants.html", plants=plant,
                    last_page=last_page, total=total,
                    next_page=next_page, selfs_page=selfs_page,
                    first_page=first_page)
        else:
            return render_template(
                "trefle_oops.html")


# Trefle Filter
# next filters


@app.route("/next_filter")
def next_filter():
    include = "filter"
    filters = "flower_color"
    query = color_filter
    page = request.args.get('page', type=int)
    plants = requests.get(
        url_all_plants + include + pre + filters
        + after + query + page_url + str(page),
        headers=headers).json()
    if plants:
        plant = plants['data']
        total = plants['meta']['total']
        links = plants['links']
        adjust_page = len(links['first'])-1
        selfs_page = links['self'][int(adjust_page):]
        first_page = links['first'][int(adjust_page):]
        prev_page = page - 1
        next_page = page + 1
        last_page = links['last'][int(adjust_page):]
        all_pages = list(range(int(first_page), int(last_page)))
        if int(last_page) == 3:
            return render_template(
                "filter_plants_three.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                all_pages=all_pages, page=page,
                prev_page=prev_page, selfs_page=selfs_page)
        if int(last_page) <= 2:
            return render_template(
                "filter_plants_two.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                all_pages=all_pages, page=page,
                prev_page=prev_page, selfs_page=selfs_page)
        if int(last_page) == int(next_page):
            return render_template(
                "filter_plants_last.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                all_pages=all_pages, page=page,
                prev_page=prev_page, selfs_page=selfs_page)
        if int(selfs_page) == int(first_page):
            return render_template(
                "filter_plants_first.html", plants=plant,
                last_page=last_page, total=total,
                next_page=next_page, first_page=first_page,
                all_pages=all_pages, page=page,
                prev_page=prev_page, selfs_page=selfs_page)
        else:
            return render_template(
                "filter_plants.html", plants=plant,
                last_page=last_page, total=total,
                prev_page=prev_page,
                next_page=next_page, selfs_page=selfs_page,
                first_page=first_page, all_pages=all_pages)
    else:
        return render_template(
            "trefle_oops.html")


# Plant.ID image search
@app.route("/plant_id")
def plant_id():
    return render_template(
            "plant_id.html")


@app.route("/get_plant_id", methods=["GET", "POST"])
def get_plant_id():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        filename = "my_image.jpg"
        file.save(os.path.join(app.config['IMAGE_UPLOADS'], filename))
        image1 = Image.open(
            os.path.join(app.config['IMAGE_UPLOADS'], "my_image.jpg"))
        image1.thumbnail((300, 300))
        image1.save(os.path.join(app.config['IMAGE_UPLOADS'], "thumbnail.jpg"))
        # encode image to base64
        with open(
            os.path.join(app.config[
                'IMAGE_UPLOADS'], "thumbnail.jpg"), "rb") as file:
            images = [base64.b64encode(file.read()).decode("ascii")]
        your_api_key = os.environ.get("your_api_key")
        json_data = {
            "images": images,
            "modifiers": ["similar_images"],
            "plant_details": [
                "common_names", "url", "wiki_description", "taxonomy"]
        }
        response = requests.post(
            "https://api.plant.id/v2/identify", json=json_data,
            headers={
                "Content-Type": "application/json",
                "Api-Key": your_api_key
                    }).json()
        if response:
            media = response["images"][0]["url"]
            for suggestion in response['suggestions']:
                plant_name = suggestion["plant_name"]
                wiki_descr = suggestion["plant_details"]["wiki_description"]
                if suggestion["similar_images"] is not None:
                    similar_images = suggestion["similar_images"]
                    for similar in similar_images:
                        url_small = similar['url_small']
                        similarity = similar['similarity']*100
                else:
                    print('None')
                if os.path.exists(
                    os.path.join(
                        app.config['IMAGE_UPLOADS'], "my_image.jpg")):
                    os.remove(
                        os.path.join(
                            app.config['IMAGE_UPLOADS'], "my_image.jpg"))
                else:
                    print("hey, file doesn't exist!")
                if os.path.exists(
                    os.path.join(
                        app.config['IMAGE_UPLOADS'], "thumbnail.jpg")):
                    os.remove(
                        os.path.join(
                            app.config['IMAGE_UPLOADS'], "thumbnail.jpg"))
                else:
                    print("hey, file doesn't exist!")
                return render_template(
                    "plant_id_deets.html", response=response,
                    plant_name=plant_name,
                    similar_images=similar_images, wiki_descr=wiki_descr,
                    url_small=url_small, similarity=similarity,
                    media=media)
        else:
            return render_template(
                "plant_id_oops.html")
    else:
        flash("Load an image first to submit!")
    return redirect(url_for("plant_id"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
