# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models import book
# replace Name for method name


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
    # Now we use class methods to query our database

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        return connectToMySQL('books_schema').query_db(query, data)

    @ classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting. #(change name in '  ')
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append ou r instances of friends
        authors = []
        # Iterate over the db results and create instances of friends with cls.
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_author_and_books(cls, data):
        # a left join to put gather a dojo and all of its ninjas
        query = "SELECT * FROM authors LEFT JOIN favorite_books ON favorite_books.author_id = authors.id LEFT JOIN books ON favorite_books.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(
            'books_schema').query_db(query, data)
        print(results)
        this_author = cls(results[0])
        # to check if data is being printed print(results)
        for data in results:
            book_data = {
                "id": data["id"],
                "title": data["title"],
                "num_of_pages": data["num_of_pages"],
                "created_at": data["created_at"],
                "updated_at": data["updated_at"]
            }
        this_author.books.append(book.Book(book_data))
        return this_author

    @classmethod
    def add_author_favorite_book(cls, data):
        # a left join to put gather a dojo and all of its ninjas
        query = "INSERT INTO authors LEFT JOIN favorite_books ON favorite_books.author_id = authors.id LEFT JOIN books ON favorite_books.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(
            'books_schema').query_db(query, data)
        print(results)
        this_author = cls(results[0])
        # to check if data is being printed print(results)
        for data in results:
            book_data = {
                "id": data["id"],
                "title": data["title"],
                "num_of_pages": data["num_of_pages"],
                "created_at": data["created_at"],
                "updated_at": data["updated_at"]
            }
        this_author.books.append(book.Book(book_data))
        return this_author
