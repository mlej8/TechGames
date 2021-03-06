from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

database = ["string1", "string2"]
API = "a89ffb0315bbb15cf4401353f297a3d7"

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

@app.route('/spiritgrowth', methods=["POST"])
def returnplaylist():
    data = request.get_json()
    if data.get("city"):
        res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={data.get("city")}appid={API}')
        print(res.json())
        playlist = []
        if res.json().get("main").get("temp"):
            temp = res.json().get("main").get("temp")
            if temp >= 30:
                playlist.append("Party Rock - LMFAO")
            elif temp >= 15 and temp < 30:
                playlist.append("Tick Tock - Kesha")
            elif temp >= 10 and temp < 15:
                playlist.append("Purple Haze - Jimi Hendrix")
            else:
                playlist.append("Four Seasons - Vivaldi")
        return jsonify(playlist), 201
    else:
        return {}, 400

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
