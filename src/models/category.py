from src.db import db
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey

class Category(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    # products = db.relationship('Product', backref='category', lazy=True)