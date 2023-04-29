from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from passlib.context import CryptContext

from settings import Base




class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    blogs = relationship('BlogModel', back_populates="author")
    
    
    
def hashPassword(password: str):
    pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")
    hashedPassword = pwd_cxt.hash(password)
    return hashedPassword