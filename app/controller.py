from flask import render_template, request

from . import app, db
from .model import Book


def select_all_books():
    return Book.query.all()


def insert_book(author, title, published_date):
    db.session.add(Book(author, title, published_date))
    db.session.commit()


def initialize_database():
    db.create_all()

    if len(select_all_books()) == 0:
        insert_book("Tolkien", "Hobbit", 2004)
        insert_book("Rowling", "Harry Potter", 1997)
        insert_book("Martin", "A Game of Thrones", 1996)
        insert_book("Rothfuss", "The Name of the Wind", 2007)


def select_books_by_author(author):
    return Book.query.filter_by(author=author).all()


@app.route("/books")
def display_books():
    if "author" in request.args.keys():
        return render_template("index.html", books=select_books_by_author(request.args.get("author")))
    else:
        return render_template("index.html", books=select_all_books())


def run():
    initialize_database()
    app.run()
