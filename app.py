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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
