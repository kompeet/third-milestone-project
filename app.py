#Import installed libraries and components to the Python file
from flask_pymongo import PyMongo
import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
if os.path.exists("env.py"):
    import env


#Define the app, and set the MONGO_URI
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

#App's paths, functions helping to let the user "do CRUD":create, retrieve, update, and delete recipes
mongo = PyMongo(app)

#Homepage
@app.route('/')


#Find all of the recipes
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


#Add new recipe using a form, submiting it using POST method
@app.route('/add_recipe')
def add_recipes():
    return render_template('addrecipes.html',
    categories=mongo.db.categories.find())
    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


#Host and Port set
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
