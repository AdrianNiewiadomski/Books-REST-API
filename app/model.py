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

    def __init__(self, authors, title, published_date, categories, ratings_count, average_rating=0, thumbnail=""):
        self.authors = str(authors)
        self.title = title
        self.published_date = published_date
        self.categories = str(categories)
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.thumbnail = thumbnail

    def __str__(self):
        return f"Book({self.author}, {self.title}, {self.published_date})"
