from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/')
def index():
    return redirect('/authors')


@app.route('/authors')
def authors():
    all_authors = Author.get_all()
    print(all_authors)
    return render_template('/authors.html', all_authors=all_authors)


@app.route('/authors/create_author', methods=['POST'])
def create_authors():
    data = {
        "name": request.form['name']
    }
    Author.save(data)
    return redirect('/authors')


@app.route('/author/show/<int:author_id>')
def show_author(author_id):
    data = {
        "id": author_id
    }
    get_author = Author.get_author_and_books(data)  # returns data for author
    get_books = Book.get_book_authors(data)  # returns data for books
    get_all_books = Book.get_all()
    return render_template('show.html', get_author=get_author, get_books=get_books, get_all_books=get_all_books)


@app.route('/author/add_book')
def add_favorite_book():
    data = {
        "id": request.form['add_book']
    }
    add_book = Author.add_author_favorite_book(data)
    return redirect('/authors', add_book=add_book)
