# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash
# replace Name for method name


class Message:
    def __init__(self, data):
        self.id = data['id']
        self.sender = data['sender']
        self.receiver = data['receiver']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
    # Now we use class methods to query our database

    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages ( message , created_at, updated_at, sender_id, receiver_id ) VALUES ( %(message)s , NOW() , NOW(), %(sender_id)s, %(receiver_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        print(query)
        return connectToMySQL('private_wall').query_db(query, data)

    @classmethod
    def get_my_messages(cls, data):
        query = "SELECT users.first_name as sender, users2.first_name as receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users2.id = %(id)s;"
        # query = "SELECT * FROM messages WHERE NOT user_id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('private_wall').query_db(query, data)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users
