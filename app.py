# Import installed libraries and components to the Python file
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from os import path
import re
from flask import Flask, render_template, redirect, request, url_for
if os.path.exists("env.py"):
    import env


# Define the app, and set the MONGO_URI
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)
DB = mongo.db
"""App's paths, functions helping to let the user "do CRUD":
create, retrieve, update, and delete recipes"""


# Homepage
@app.route('/')
def home():
    all_categories = list(mongo.db.categories.find())
    return render_template("index.html", categories=all_categories)


# Find recipes
"""Search for recipes with regex method,
    results of the search returned with the for loop in results.html"""


@app.route("/find_recipes")
def find_recipes():
    query = request.args.get("search")
    search_term = mongo.db.recipes.find({"ingredients": {"$regex": query}})
    search = search_term
    no_of_docs = mongo.db.recipes.count_documents(
     {"ingredients": {"$regex": query}})
    all_categories = list(mongo.db.categories.find())
    return render_template(
        "result.html",
        categories=all_categories,
        search=search_term, no_of_docs=no_of_docs)


@app.route('/get_recipes')
def get_recipes():
    # List of the recipes with find() method
    all_categories = list(mongo.db.categories.find())
    return render_template(
        "recipes.html",
        categories=all_categories, recipes=mongo.db.recipes.find())


# Add new recipe using a form, submiting it using POST method
@app.route('/add_recipe')
def add_recipe():
    all_categories = list(mongo.db.categories.find())
    return render_template(
        'addrecipes.html',
        categories=all_categories)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


# Find a recipe by its ID then render the editrecipe HTML file
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = list(mongo.db.categories.find())
    return render_template(
        'editrecipe.html',
        recipe=the_recipe, categories=all_categories)


# Update the article after editing it using JSON
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)}, {
        'title': request.form.get('title'),
        'ingredients': request.form.get('ingredients'),
        'steps': request.form.get('steps'),
        'category_name': request.form.get('category_name'),
        'picture': request.form.get('picture')})
# When the recipe is updated, redirect the user to the list of recipes
    return redirect(url_for('get_recipes'))


# Delete recipe selected by ID then redirect the user to the list of recipes
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


# Get Categories
"""  Get and display categories, so the user can click on the category_name
    and the list of the recipes"""


@app.route('/get_categories')
def get_categories():
    return render_template(
        'categories.html',
        categories=mongo.db.categories.find())


@app.route('/display_categories/<category_name>')
def display_categories(category_name):
    all_recipe = mongo.db.recipes.find({"category_name": category_name})
    all_categories = list(mongo.db.categories.find())
    return render_template(
     'displaycategories.html', recipes=all_recipe, category=category_name,
     categories=all_categories)


# Displaying cards with split method
@app.route('/display_recipe/<recipe_id>')
def display_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = the_recipe["ingredients"].split(";")
    steps = the_recipe["steps"].split(";")
    all_categories = list(mongo.db.categories.find())
    return render_template(
        'recipe_page.html', recipe=the_recipe,
        categories=all_categories, ingredients=ingredients, steps=steps)


# Host and Port set
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=False)
