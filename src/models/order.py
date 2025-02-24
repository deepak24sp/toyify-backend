from src.db import db
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship

class Order(db.Model):
    __tablename__ = 'orders'
    
    orderid = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, db.ForeignKey('users.user_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)
    
    user = relationship("User", backref="orders")
    
    def __repr__(self):
        return f'<Order {self.orderid} - User {self.userid}>'
