from src.db import db
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship

class ProductImage(db.Model):
    __tablename__ = 'product_images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id', ondelete="CASCADE"))
    image_url = Column(String(500), nullable=True)
    product = relationship("Product", back_populates="images")