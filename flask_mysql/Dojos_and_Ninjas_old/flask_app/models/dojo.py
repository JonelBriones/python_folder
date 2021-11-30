# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.ninja import Ninja
# replace Name for method name


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(dojo_name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age, dojo_id , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(age)s, %(id)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_id(cls, data):
        query = "SELECT * FROM dojos WHERE name = %(location)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data_id):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data_id)
        return (cls(results[0]))

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_dojo_and_ninjas(cls, data):
        # a left join to put gather a dojo and all of its ninjas
        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        this_dojo = cls(results[0])
        # to check if data is being printed print(results)
        for ninja in results:
            ninja_data = {
                "id": ninja["id"],
                "first_name": ninja["first_name"],
                "last_name": ninja["last_name"],
                "age": ninja["age"],
                "dojo_id": ninja["id"],
                "created_at": ninja["created_at"],
                "updated_at": ninja["updated_at"]
            }
        this_dojo.ninjas.append(Ninja(ninja_data))
        return this_dojo
