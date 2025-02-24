from src.db import db
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    order_item_id = Column(Integer, primary_key=True, autoincrement=True)
    orderid = Column(Integer, db.ForeignKey('orders.orderid'), nullable=False)
    product_id = Column(Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    
    order = relationship("Order", backref="order_items")
    product = relationship("Product", backref="order_items")
    
    def __repr__(self):
        return f'<OrderItem {self.order_item_id} - Order {self.orderid}>'
