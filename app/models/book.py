from sqlalchemy import Column, Integer, String, Text, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.sql import func
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id", onupdate="RESTRICT"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", onupdate="RESTRICT"), nullable=False)
    cover_image = Column(String(255), nullable=True) #save path, example: static/covers/xxx.jpg
    created_at = Column(DATETIME(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DATETIME(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
#Relationships wihth Author and Category
    author = relationship("Author", back_populates="books")
    category = relationship("Category", back_populates="books")