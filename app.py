from flask import Flask, jsonify, request
import os

app = Flask(__name__)

database = ["string1", "string2"]

@app.route('/', methods=["GET"])
def hello_world():
    return 'Hello, World!'

@app.route('/status', methods=["GET"])
def get_func():
    return {"status": "up"}, 200

@app.route('/processPathData/<pathParameter>', methods=["GET"])
def echo_path(pathParameter):
    return {"pathParam": pathParameter} , 200 

@app.route('/processPOSTData', methods=["POST"])
def postdata():
    data = request.get_json()
    values = list(data.values())
    return {"values": values}, 200

@app.route('/processQueryData', methods=["GET"])
def queryParams():
    d = request.args.to_dict()
    if d:
        return d, 200
    else:
        return "Query parameters must not be empty", 400

### DATABASE

@app.route('/data', methods=["GET"])
def data():
    return jsonify(database)

@app.route('/data/add', methods=["POST"])
def adddata():
    data = request.get_json()
    if data.get("newString"):
        database.append(data.get("newString"))
        print(database)
        return "", 201
    else:
        return "", 400

@app.route("/data/<int:index>", methods=["DELETE"])
def delete(index):
    if index >= len(database):
        return "Index out of range", 400
    else:
        print("database before ", database)
        database.pop(index)
        print("database after ", database)
        return "",200 

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run()
