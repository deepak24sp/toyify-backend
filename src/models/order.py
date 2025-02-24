from src.db import db
from sqlalchemy import Column, Integer, Float, String,ForeignKey
from sqlalchemy.orm import relationship

class Order(db.Model):
    __tablename__ = 'orders'
    
    orderid = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)
    
    
    def __repr__(self):
        return f'<Order {self.orderid} - User {self.userid}>'
