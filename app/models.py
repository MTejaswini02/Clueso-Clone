
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    feedbacks = relationship("Feedback", back_populates="user")
    




class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    message = Column(String(255), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="feedbacks")
