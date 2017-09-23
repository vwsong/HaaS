"""
$ pip install Flask
$ FLASK_APP=main.py flask run
 * Running on http://localhost:5000/
"""

from hashmap import Hashmap
from flask import Flask
from flask import Response
from flask import json
from flask import request
app = Flask(__name__)

db = {}

@app.route("/")
def hello():
    data = {
        'hello'  : 'world!'
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route("/create", methods = ["POST"])
def create():
    db_id = request.json["id"]
    size = request.json["size"]

    if db_id in db:
        return "Database " + str(db_id) + " already set!"
    else:
        db[db_id] = Hashmap(int(size))
    return "Data set!"

@app.route("/set", methods = ["POST"])
def set():
    db_id = request.json["id"]
    key = request.json["key"]
    value = request.json["value"]

    if db_id in db:
        currDB = db[db_id]
        currDB.set(key, value)
    else:
        return "Database " + str(db_id) + " not set."
    return "Data set!"

@app.route("/get", methods = ["GET"])
def get():
    if "id" in request.args:
        db_id = request.args["id"]
    else:
        return "Please enter an ID"

    if "key" in request.args:
        key = request.args["key"]
    else:
        return "Please enter a key"

    output = db[db_id].get(key)
    if output:
        return output
    else:
        return "Key not set."

@app.route("/load", methods = ["GET"])
def get():
    if "id" in request.args:
        db_id = request.args["id"]
    else:
        return "Please enter an ID"

    output = db[db_id].load()
    if output:
        return output
    else:
        return "Key not set"

@app.route("/delete", methods = ["POST"])
def delete():
    db_id = request.json["id"]
    key = request.json["key"]

    if not db_id or not key:
        return "Invalid parameters"

    if db_id in db:
        output = db[db_id].delete(key)
        if output:
            return "Deleted"
        else:
            return "Key invalid"
