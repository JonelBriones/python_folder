# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the friend table from our database

# replace Name for method name


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @staticmethod
    def validate_dojo(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 character.")
            is_valid = False
        if len(survey['location']) < 3:
            flash("Please choose one Location.")
            is_valid = False
        if len(survey['language']) < 3:
            flash("Please choose one Language.")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name , location , language, comment , created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        print(query)
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
