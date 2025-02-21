from src.db import db
from sqlalchemy import Column,Integer,String,JSON,Float
from sqlalchemy.orm import relationship

class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer,primary_key=True,autoincrement=True)
    category_id = Column(Integer, db.ForeignKey('category.id'), nullable=False)
    name = Column(String(50),nullable=False)
    price = Column(Float, nullable=False)
    description = Column(JSON, nullable=True)
    images = relationship("ProductImage", back_populates="product", lazy=True)