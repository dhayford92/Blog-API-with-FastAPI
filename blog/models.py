from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from settings import Base








class BlogModel(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    publish = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    author = relationship('UserModel', back_populates="blogs")
    
    
    

    
