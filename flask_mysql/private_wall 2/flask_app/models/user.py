# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.login import Login
from flask import flash
import re  # for regex
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)    # we are creating an object called bcrypt,
# which is made by invoking the function Bcrypt with our app as an argument


# replace Name for method name

# to pattern validate for emails
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email, password, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s, %(password)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        print(query)
        return connectToMySQL('private_wall').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('private_wall').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        print(users)
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(
            'private_wall').query_db(query, data)
        if len(results) == 0:
            return False
        return (cls(results[0]))
    # Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger

    @staticmethod
    def validate_register(user):
        is_valid = True  # we assume this is true
        if len(user['fname']) < 1:
            flash("First Name cannot be blank.", "register")
            is_valid = False
        if len(user['lname']) < 1:
            flash("Last Name cannot be blank.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", "register")
            is_valid = False
        email = {'email': user['email']}
        user_email = Login.get_by_email(email)
        if user_email:
            flash("This email is taken", "register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "register")
            is_valid = False
        if (user['password']) != (user['cpassword']):
            flash("Confirmed password must match Password!", "register")
        return is_valid
