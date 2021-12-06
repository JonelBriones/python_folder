# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
import re
from flask import flash
# replace Name for method name
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @staticmethod
    def success():
        is_valid = True
        flash("Email is Valid!")
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails ( email , created_at, updated_at ) VALUES ( %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('email_validation_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('email_validation_schema').query_db(query)
        # Create an empty list to append our instances of friends
        emails = []
        # Iterate over the db results and create instances of friends with cls.
        for email in results:
            emails.append(cls(email))
        return emails
