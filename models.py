# # Defines the Blog model for the database using SQLAlchemy ORM.

# from sqlalchemy import Column, Integer, String, Text
# from database import Base

# # Blog Table
# class Blog(Base): # Represents the "blogs" table in the database, inheriting from the Base class defined in database.py. This class defines the structure of the table and its columns.
#     __tablename__ = "blogs"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     content = Column(Text)

from sqlalchemy import Column, Integer, String, Text
from database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True ,index=True)
    title = Column(String)
    content = Column(Text)