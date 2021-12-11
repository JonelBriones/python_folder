# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash
# replace Name for method name
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)    # we are creating an object called bcrypt,
# which is made by invoking the function Bcrypt with our app as an argument

# to pattern validate for emails


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date = data['date']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    # Now we use class methods to query our database
########## CREATE RECIPES ############

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes ( name , description , instruction, date, time, created_at, updated_at, user_id ) VALUES ( %(name)s , %(description)s , %(instruction)s, %(date)s, %(time)s, NOW() , NOW(), %(user_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        print(query)
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        print(query)
        return connectToMySQL('recipes').query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True  # we assume this is true
        if len(recipe['name']) < 3:
            flash("name must be at least 3 characers.", "recipe")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("description must be at least 3 characers.", "recipe")
            is_valid = False
        if len(recipe['instruction']) < 3:
            flash("Instruction must be at least 3 characters.", "recipe")
            is_valid = False
        return is_valid

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s , description = %(description)s  , instruction = %(instruction)s, date = %(date)s, time = %(time)s, updated_at = NOW() WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        print(query)
        return connectToMySQL('recipes').query_db(query, data)

########## COLLECT ALL RECIPES ############

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM recipes WHERE user_id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('recipes').query_db(query, data)
        # Create an empty list to append our instances of friends
        recipes = []
        # Iterate over the db results and create instances of friends with cls.
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

########## Gather recipe data from specfic ID #########
    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(
            'recipes').query_db(query, data)
        if len(results) == 0:
            return False
        return (cls(results[0]))
