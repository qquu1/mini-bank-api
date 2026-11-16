from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index = True)
    username = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True) 
    is_admin = Column(Boolean, default=False)

    account = relationship("Account", back_populates="owner", uselist=False, cascade="all, delete-orphan")

    profile = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    ##вот из ит сверху