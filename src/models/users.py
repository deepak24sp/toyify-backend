from src.db import db
from sqlalchemy import Column, Integer, String, JSON,CheckConstraint
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    mobile_number = Column(String(10), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    user_type = Column(String(20), nullable=False)
    address = Column(JSON, nullable=True)

    orders = relationship("Order", backref="user")

    __table_args__ = (
        CheckConstraint("user_type IN ('admin', 'customer')", name="check_user_type"),
    )
    
    def __repr__(self):
        return f'<User {self.user_id} - {self.name}>'
