import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'plant_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_plants")
def get_plants():
    return render_template("plants.html",
                           plants=mongo.db.plants.find())


@app.route("/add_plants")
def add_plants():
    return render_template("addplants.html",
                           collections=mongo.db.collections.find())


@app.route("/insert_plant", methods=["POST"])
def insert_plant():
    plants = mongo.db.plants
    plants.insert_one(request.form.to_dict())
    return redirect(url_for("get_plants"))


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
        "image_url": request.form.get("image_url")
    })
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


@app.route("/insert_collection", methods=["POST"])
def insert_collection():
    collection = mongo.db.collections
    collection.insert_one(request.form.to_dict())
    return redirect(url_for("get_collections"))


@app.route('/edit_collection/<collection_id>')
def edit_collection(collection_id):
    the_collection = mongo.db.collections.find_one({"_id": ObjectId(collection_id)})
    all_collections = mongo.db.collections.find()
    return render_template("editcollections.html", collection=the_collection,
                            collections=all_collections)


@app.route('/update_collection/<collection_id>', methods=["POST"])
def update_collection(collection_id):
    collections = mongo.db.collections
    collections.update({"_id": ObjectId(collection_id)},
    {
        "collection_name": request.form.get("collection_name"),
        "description": request.form.get("description"),
        "date_added": request.form.get("date_added"),
    })
    return redirect(url_for("get_collections"))


@app.route('/delete_collection/<collection_id>')
def delete_collection(collection_id):
    mongo.db.collections.remove({"_id": ObjectId(collection_id)})
    return redirect(url_for("get_collections"))


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

