# Schemas for Blog API using Pydantic models.

# from pydantic import BaseModel

# # Input Schema
# class BlogCreate(BaseModel):
#     title: str
#     content: str

# # Output Schema
# class BlogResponse(BaseModel):
#     id: int
#     title: str
#     content: str

#     class Config: # Pydantic configuration for the BlogResponse model.
#         from_attributes=True # This allows Pydantic to read data from ORM models (like SQLAlchemy models) and convert them into Pydantic models. Basically, it allows you to return SQLAlchemy model instances directly from your API endpoints, and Pydantic will handle the conversion to the response schema. It serializes the ORM model instances into Pydantic models, which can then be returned as JSON responses from your API endpoints. This is particularly useful when you want to expose database records through your API while maintaining a clear separation between your database models and the data you send to clients. Serialization of ORM models into Pydantic models is useful for returning data from the database in a structured format.

from pydantic import BaseModel

class BlogsCreate(BaseModel):
    title: str
    content: str

class BlogsResponse(BaseModel):
    id: int
    title: str
    content: str