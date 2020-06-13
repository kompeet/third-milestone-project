import os
from os import path
from flask import Flask
from flask_pymongo import PyMongo
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


if __name__ == '__main__':
 app.run(host=os.environ.get('IP'),
 port=int(os.environ.get('PORT')),
 debug=True)