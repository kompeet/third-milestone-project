from flask_pymongo import PyMongo
import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)

@app.route('/')

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/add_recipes')
def add_recipes():
    return render_template('addrecipes.html',
    categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
