import json
import logging

from flask import render_template, request, redirect, url_for

from app import app, db
from app.model import Book

logging.basicConfig(level=logging.DEBUG)


def select_all_books():
    logging.debug("Getting all books")
    return Book.query.all()


def insert_book(book):
    logging.debug(f"Adding {book} to database.")
    db.session.add(book)
    db.session.commit()


def initialize_database():
    db.drop_all()
    db.create_all()
    logging.debug("The database has been created.")

    insert_book(Book(["J. R. R. Tolkien"], "Hobbit czyli Tam i z powrotem", 2004))
    insert_book(Book(["Rowling"], "Harry Potter", 1997))
    insert_book(Book(["Martin"], "A Game of Thrones", 1996))
    insert_book(Book(["Rothfuss"], "The Name of the Wind", 2007))
    insert_book(Book(["W. Krysicki", "L. Wlodarski"], "Analiza matematyczna w zadaniach", 2003))
    insert_book(Book(["R. C. Martin"], "Czysty kod", 2009))
    insert_book(Book(["M. Lutz"], "Python. Wprowadzenie", 2011))


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
    logging.debug(f"Book selected by id: {book}")
    return book.to_json()


def update_book(old_book, new_book):
    old_book.published_date = new_book.published_date
    old_book.categories = new_book.categories
    old_book.average_rating = new_book.average_rating
    old_book.ratings_count = new_book.ratings_count
    old_book.thumbnail = new_book.thumbnail
    logging.debug(f"Updating {new_book}.")
    db.session.commit()


@app.route("/db", methods=["POST"])
def update_database():
    data = json.loads(request.data.decode('utf8'))
    logging.info(f"The following data has been received: {data}")
    new_book = Book(**data)

    books = select_all_books()
    for book in books:
        if book == new_book:
            update_book(book, new_book)
            return "<h1>Success!</h1><p>A book has been updated.</p>"
    insert_book(new_book)
    return "<h1>Success!</h1><p>A new book has been inserted.</p>"


@app.errorhandler(404)
def page_not_found(e):
    logging.debug("Invalid url entered")
    return f"<h1>404</h1><p>{str(e)}</p>", 404


initialize_database()

# Nie wrzucac do pythonanywhere
if __name__ == "__main__":
    app.run(debug=True)
