from sqlalchemy import Column, Integer, String

from . import db


class Book(db.Model):
    id = Column("id", Integer, primary_key=True)
    author = Column("author", String(20), nullable=False)
    title = Column(String(100), nullable=False)
    published_date = Column(Integer)

    def __init__(self, author, title, published_date):
        self.author = author
        self.title = title
        self.published_date = published_date

    def __str__(self):
        return f"Book({self.author}, {self.title}, {self.published_date})"
