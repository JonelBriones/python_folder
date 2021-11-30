# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class Ninja:
    def __init__(self, data):
        self.id = data['id']  # ['from dojo.py']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age, dojo_id , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(age)s, %(dojo_id)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(fname)s , last_name = %(lname)s , age = %(age)s, updated_at = NOW()  WHERE ninjas.id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "Select * FROM ninjas WHERE ninjas.id = %(id)s;"
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        return (cls(results[0]))

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE ninjas.id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
