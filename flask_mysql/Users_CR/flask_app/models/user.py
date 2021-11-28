from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('Users_CR').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(fname)s , last_name = %(lname)s , email = %(email)s, updated_at = NOW()  WHERE users.id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('Users_CR').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "Select * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL('Users_CR').query_db(query, data)
        return (cls(results[0]))

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE users.id = %(id)s;"
        return connectToMySQL('Users_CR').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('Users_CR').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users
