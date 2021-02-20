from flask import Flask, jsonify, request
import os

app = Flask(__name__)

database = ["string1", "string2"]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/status')
def get_func():
    res = {
        "status": "up"
    }
    return jsonify(res)

@app.route('/processPathData/<pathParameter>')
def echo_path(pathParameter):
    res = {
        "pathParam": pathParameter
    }
    return jsonify(res)

@app.route('/data')
def data():
    return jsonify(database)

@app.route('/data/add', methods=["POST"])
def adddata():
    data = request.get_json()
    if data.get("newString"):
        database.append(data.get("newString"))
        print(database)
        return {}, 201
    else:
        return {}, 400

@app.route('/processPOSTData', methods=["POST"])
def postdata():
    # TODO: Handle the edge cases - Handle empty json, etc.  empty json 
    data = request.get_json()
    values = list(data.values())
    return {"values": values}, 200

@app.route('/processQueryData', methods=["GET"])
def queryParams():
    # TODO: Handle the edge cases.
    return request.args.to_dict(), 200

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run()
