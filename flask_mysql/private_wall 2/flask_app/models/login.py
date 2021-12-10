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


class Login:
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
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users

    # @classmethod
    # def get_one_complete(cls,data):
    #     query = "SELECT FROM users WHERE users.id = %(id)s;"
    #     results = connectToMySQL('login_and_registration').query_db(query)
    #     user = (cls(results[0]))

    #     if results[0]['users.id'] == None:
    #         return (cls(results[0]))
    #     else:
    #         for user in results:
    #             user_data = {
    #                 'id' : user['user.id'],
    #                 'first_name' : user['user.first_name'],
    #                 'last_name' : user['user.last_name'],
    #                 'email' : user['user.email'],
    #                 'password' : user['user.password'],
    #                 'created_at' : user['user.created_at'],
    #                 'updated_at' : user['user.updated_at'],
    #             }
    #             user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(
            "private_wall").query_db(query, data)
        if len(results) == 0:
            return False
        else:
            return cls(results[0])

    @staticmethod
    def validate_login(formData):
        is_valid = True

        email = {"email": formData['email']}
        user = Login.get_by_email(email)

        if not user:
            flash("Invalid Email/Password")
            is_valid = False
        if not bcrypt.check_password_hash(user.password, formData['password']):
            flash("Invalid Email/Password")
            is_valid = False
        return is_valid
