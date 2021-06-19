from flask import render_template, request, redirect, url_for
import logging
from . import app, db
from .model import Book
logging.basicConfig(level=logging.DEBUG)


def select_all_books():
    return Book.query.all()


def insert_book(author, title, published_date):
    db.session.add(Book(author, title, published_date, "", 0))
    db.session.commit()


def initialize_database():
    db.create_all()

    if len(select_all_books()) == 0:
        insert_book("Tolkien", "Hobbit", 2004)
        insert_book("Rowling", "Harry Potter", 1997)
        insert_book("Martin", "A Game of Thrones", 1996)
        insert_book("Rothfuss", "The Name of the Wind", 2007)


# def select_books_by_authors(authors):
#     return Book.query.filter_by(authors=authors).all()

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
            # return render_template("index.html", books=select_books_by_authors(request.args.get("author")))

        elif "published_date" in request.args.keys():
            logging.debug("published_date in request.args.keys()")
            return render_template("index.html",
                                   books=select_books_by_published_date(request.args.get("published_date")))

        elif "sort" in request.args.keys():
            logging.debug("sort in request.args.keys()")
            return render_template("index.html", books=sort_books_by_published_date(request.args.get("sort")))

        else:
            logging.debug("else")
            return redirect(url_for("display_books"))
    else:
        return render_template("index.html", books=select_all_books())


@app.errorhandler(404)
def page_not_found(e):
    return f"<h1>404</h1><p>{str(e)}</p>", 404


def run():
    initialize_database()
    app.run()
