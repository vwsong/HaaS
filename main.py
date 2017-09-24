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

    data = {
        "Code" : "200",
        "message" : "Success - Data set!"
    }

    if db_id in db:
        data = {
            "Code" : "400",
            "message" : "Database " + str(db_id) + " already set!"
        }
    else:
        db[db_id] = Hashmap(int(size))

    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route("/set", methods = ["POST"])
def set():
    db_id = request.json["id"]
    key = request.json["key"]
    value = request.json["value"]

    data = {
        "Code" : "200",
        "message" : "Success - Data set!"
    }

    if db_id in db:
        currDB = db[db_id]
        success = currDB.set(key, value)
        if not success:
            data = {
                "Code" : "400",
                "message" : "Failure - hashmap is full."
            }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    else:
        data = {
            "Code" : "400",
            "message" : "Database " + str(db_id) + " doesn't exist!"
        }
        js = json.dumps(data)
        resp = Response(js, status=400, mimetype='application/json')
    return resp

@app.route("/get", methods = ["GET"])
def get():

    if "id" in request.args and "key" in request.args:
        db_id = request.args["id"]
        key = request.args["key"]

        output = db[db_id].get(key)
        if output:
            data = {
                "Code" : "200",
                "Value" : str(output)
            }
            js = json.dumps(data)
            resp = Response(js, status=200, mimetype='application/json')
            return resp
        else:
            data = {
                "Code" : "400",
                "message" : "Key not set."
            }
            js = json.dumps(data)
            resp = Response(js, status=400, mimetype='application/json')
            return resp
    else:
        data = {
            "Code" : "400",
            "message" : "Key not set."
        }
        js = json.dumps(data)
        resp = Response(js, status=400, mimetype='application/json')
        return resp

@app.route("/load", methods = ["GET"])
def load():
    if "id" in request.args:
        db_id = request.args["id"]
        output = db[db_id].load()

        data = {
            "Code" : "200",
            "value" : output
        }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    else:
        data = {
            "Code" : "400",
            "message" : "Please enter an ID"
        }
        js = json.dumps(data)
        resp = Response(js, status=400, mimetype='application/json')

    return resp

@app.route("/delete", methods = ["POST"])
def delete():
    db_id = request.json["id"]
    key = request.json["key"]

    if not db_id or not key:
        data = {
            "Code" : "400",
            "message" : "Invalid parameters"
        }
        js = json.dumps(data)
        resp = Response(js, status=400, mimetype='application/json')
        return resp

    if db_id in db:
        output = db[db_id].delete(key)
        if output:
            data = {
                "Code" : "200",
                "value" : output
            }
            js = json.dumps(data)
            resp = Response(js, status=200, mimetype='application/json')
            return resp
        else:
            data = {
                "Code" : "400",
                "message" : "Key doesn't exist."
            }
            js = json.dumps(data)
            resp = Response(js, status=400, mimetype='application/json')
            return resp
    else:
        data = {
            "Code" : "400",
            "message" : "DB doesn't exist."
        }
        js = json.dumps(data)
        resp = Response(js, status=400, mimetype='application/json')
        return resp
