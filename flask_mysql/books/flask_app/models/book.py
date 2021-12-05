# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models import author
# replace Name for method name


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
    # Now we use class methods to query our database

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books ( title , num_of_pages , created_at, updated_at ) VALUES ( %(title)s , %(num_of_pages)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append ou r instances of friends
        books = []
        # Iterate over the db results and create instances of friends with cls.
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_one(cls):
        query = "SELECT * FROM books WHERE books.id = %(id)s;"
        return connectToMySQL('books_schema').query_db(query)

    @classmethod
    def get_book_authors(cls, data):
        # a left join to put gather a dojo and all of its ninjas
        query = "SELECT * FROM books LEFT JOIN favorite_books ON favorite_books.book_id = books.id LEFT JOIN authors ON favorite_books.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(
            'books_schema').query_db(query, data)
        this_book = cls(results[0])
        # to check if data is being printed print(results)
        for data in results:
            author_data = {
                "id": data["id"],
                "name": data["name"],
                "created_at": data["created_at"],
                "updated_at": data["updated_at"]
            }
        this_book.authors.append(author.Author(author_data))
        return this_book
