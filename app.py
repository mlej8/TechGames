from flask import Flask
from flask import jsonify
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

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run()
