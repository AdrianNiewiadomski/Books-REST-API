from sqlalchemy import Column, Integer, String, Float

from . import db


class Book(db.Model):
    id = Column("id", Integer, primary_key=True)
    authors = Column("authors", String(200), nullable=False)
    title = Column(String(100), nullable=False)
    published_date = Column(String(10), nullable=False)
    categories = Column(String(200))
    average_rating = Column(Float)
    ratings_count = Column(Integer)
    thumbnail = Column(String(100))

    def __init__(self, authors, title, published_date, categories=None, average_rating=0, ratings_count=0,
                 thumbnail=""):
        self.authors = Book._get_string_from_list(authors)
        self.title = title
        self.published_date = published_date
        if categories is None:
            categories = [""]
        self.categories = Book._get_string_from_list(categories)
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.thumbnail = thumbnail

    def __str__(self):
        return f"Book({self.authors}, {self.title}, {self.published_date})"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.authors == other.authors and self.title == other.title
        else:
            return False

    @staticmethod
    def _get_string_from_list(list_of_strings):
        string_from_list = list_of_strings.pop(0)
        if len(list_of_strings) > 0:
            for item in list_of_strings:
                string_from_list += ', ' + item
        return string_from_list

    def to_json(self):
        return {
            "title": self.title,
            "authors": self.authors.split(", "),
            "published_date": self.published_date,
            "categories": self.categories.split(", "),
            "average_rating": self.average_rating,
            "ratings_count": self.ratings_count,
            "thumbnail": self.thumbnail
        }
