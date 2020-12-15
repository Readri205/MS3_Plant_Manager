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


ENDPOINT = "https://trefle.io/api/v1/plants/search?"
ALLPLANTSENDPOINT = "https://trefle.io/api/v1/plants?"
HTTPS = "https://trefle.io"
FORWARD = "/"
ALLPLANTS = "/api/v1/species?"
ONESPECIES = "/api/v1/species/"
PLANTSEARCH = "/api/v1/species/search?"
YOUR_TREFLE_TOKEN = os.environ.get("YOUR_TREFLE_TOKEN")
TOK = "token="
FILTER1 = "&filter"
FILTERNOT = "&filter_not[common_name]=None"
RANGE1 = "&range"
FILTERCRITERIA1 = "[flower_color]="
FILTERSEARCH1 = "blue"
RANGECRITERIA1 = "[light]="
RANGESEARCH1 = ",9"
SEARCH = "yarrow"
SEARCH_SPECIES = "lily"
PAGE = "&page="
NUMBER = "2"
STRG = "&q="
query = "yarrow"

ENDPOINT_SPECIES = "https://trefle.io/api/v1/species/search?"
FILTER = "&filter[common_name]=rose"
ID = '183086'

url = HTTPS + PLANTSEARCH + TOK + YOUR_TREFLE_TOKEN + STRG + query
url_page_no = HTTPS + PLANTSEARCH + TOK + YOUR_TREFLE_TOKEN + "&"
url_test = HTTPS + PLANTSEARCH + TOK + YOUR_TREFLE_TOKEN + PAGE + NUMBER + STRG + query
url_search = HTTPS + PLANTSEARCH + TOK + YOUR_TREFLE_TOKEN + PAGE

next_page = False
prev_page = False





def trefle_get():
    results = requests.get(url).json()
    plants = results['data']
    for i in plants:
        common_name = i['common_name']
        print(common_name)


# trefle_get()


def trefle_next():
    results = requests.get(url).json()
    links = results['links']
    if 'next' in links:
        nexts = links['next']
        page_no = nexts[23:]
        results = requests.get(url_page_no + page_no).json()
        return (next_page)
#    while next_page:
#        data = request.get(url).json()
        print(json.dumps(results, indent=2))
#    print(json.dumps(links, indent=2))


# trefle_next()


def trefle_while():
    plants = []
    results = requests.get(url).json()
    plants = results["data"]
    links = results['links']
    if 'next' in links:
        nexts = links['next']
        page_no = nexts[23:]
        results = requests.get(url_page_no + page_no).json()
        print(nexts)
    while 'next':
        nexts = links['next']
        page_no = nexts[23:]
        results = requests.get(url_page_no + page_no).json()
        plants.extend(results)
    print(json.dumps(results, indent=2))
#    for plant in plants:
#        common_name = plant['common_name']
#        print(common_name)

    # printing plant common name
#    for i, plant in enumerate(plants):
#        print(i, plant['common_name'])


# trefle_while()


def trefle_pages():
    plants = requests.get(url).json()
    links = plants['links']
    first = links['first'][28:]
    first_many = len(first)
    query_adjust = len(query) + 3
    first_net_adjust = first_many - query_adjust
    first_no_pages = first[:first_net_adjust]
    if 'next' in links:
        nexts = links['next'][23:]
        nexts_many = len(nexts)
        nexts_net_adjust = nexts_many - query_adjust
        nexts_no_pages = nexts[:nexts_net_adjust]
        last = links['last'][28:]
        last_many = len(last)
        last_net_adjust = last_many - query_adjust
        last_no_pages = last[:last_net_adjust]
        print(nexts, first_no_pages, nexts_no_pages, last_no_pages)
        results = requests.get(url_page_no + nexts).json()
        print(json.dumps(results['links'], indent=2))
    else:
        print(first_no_pages)


# trefle_pages()


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
