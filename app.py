#Import installed libraries and components to the Python file
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
def add_recipe():
    return render_template('addrecipes.html',
    categories=mongo.db.categories.find())
    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


#Find a recipe by its ID then render the editrecipe HTML file
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           categories=all_categories)    


#Host and Port set
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
