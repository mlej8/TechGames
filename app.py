from flask import Flask, jsonify, request
import os

app = Flask(__name__)
database = []

@app.route('/')
def hello_world():
    return 'Hello, World!'

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
