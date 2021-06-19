import logging

from flask import render_template, request, redirect, url_for

from . import app, db
from .model import Book

logging.basicConfig(level=logging.DEBUG)


def select_all_books():
    logging.debug("Getting all books")
    return Book.query.all()


def insert_book(author, title, published_date):
    book = Book(author, title, published_date, "", 0)
    logging.debug(f"Adding {book} to database.")
    db.session.add(book)
    db.session.commit()


def initialize_database():
    db.create_all()
    logging.debug("The database has been created.")

    if len(select_all_books()) < 7:
        # insert_book("Tolkien", "Hobbit", 2004)
        # insert_book("Rowling", "Harry Potter", 1997)
        # insert_book("Martin", "A Game of Thrones", 1996)
        # insert_book("Rothfuss", "The Name of the Wind", 2007)
        # insert_book(["W. Krysicki", "L. Wlodarski"], "Analiza matematyczna w zadaniach", 2003)
        # insert_book("R. C. Martin", "Czysty kod", 2009)
        insert_book("M. Lutz", "Python. Wprowadzenie", 2011)


def select_books_by_authors(args):
    authors = dict(args.lists())["author"]
    logging.debug(f"Filtering books by authors. ({authors})")

    if "" in authors:
        authors.remove("")
    if len(authors) == 1:
        return Book.query.filter(Book.authors.contains(authors[0])).all()
    return Book.query.filter(Book.authors.contains(authors[0])).filter(Book.authors.contains(authors[1])).all()


def select_books_by_published_date(published_date):
    logging.debug(f"Filtering books by published date. ({published_date})")
    return Book.query.filter_by(published_date=published_date).all()


def sort_books_by_published_date(order):
    if "-" in order:
        logging.debug("Sorting books in descending order.")
        return Book.query.order_by(Book.published_date.desc()).all()
    logging.debug("Sorting books in ascending order.")
    return Book.query.order_by(Book.published_date).all()


@app.route("/books")
def display_books():
    if request.args:
        logging.debug(f"\nThe following data has been received: {request.args}")
        if "author" in request.args.keys():
            logging.debug("author in request.args.keys()")
            return render_template("index.html", books=select_books_by_authors(request.args))

        elif "published_date" in request.args.keys():
            logging.debug("published_date in request.args.keys()")
            return render_template("index.html",
                                   books=select_books_by_published_date(request.args.get("published_date")))

        elif "sort" in request.args.keys():
            logging.debug("sort in request.args.keys()")
            return render_template("index.html", books=sort_books_by_published_date(request.args.get("sort")))

        else:
            logging.debug("Invalid url entered")
            return redirect(url_for("display_books"))
    else:
        logging.debug("Displaying all books.")
        return render_template("index.html", books=select_all_books())


@app.route("/books/<bookId>")
def select_book_by_id(bookId):
    book = Book.query.filter_by(id=bookId).first()
    print("Book: ", book)
    return book.to_json()


@app.errorhandler(404)
def page_not_found(e):
    logging.debug("Invalid url entered")
    return f"<h1>404</h1><p>{str(e)}</p>", 404


def run():
    initialize_database()
    app.run()
