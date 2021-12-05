from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book


@app.route('/author/add_book')
def add_book():
    get_all_books = Book.get_all()

    return render_template('new_books.html', get_all_books=get_all_books)


@app.route('/authors/create_books/process', methods=['POST'])
def add_book_process():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    print("hello")
    print(data)
    return redirect('/authors', Book.save(data))


@app.route('/book/show/<int:book_id>')
def favorited_by(book_id):
    data = {
        "id": book_id,
    }

    return render_template('show_book.html', get_book_author=Book.get_book_authors(data))
