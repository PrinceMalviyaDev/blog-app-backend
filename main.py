# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import engine, SessionLocal
# import models, schemas

# models.Base.metadata.create_all(bind=engine)  # Create the database tables based on the defined models. This line ensures that the database schema is created according to the SQLAlchemy models defined in models.py. It uses the metadata of the Base class to create all tables in the database that are defined as subclasses of Base. This is typically done at application startup to ensure that the necessary tables exist before any API operations are performed.

# app = FastAPI()

# # DB Dependency
# def get_db():  # This function is a "dependency" that provides a database session to the API endpoints. It creates a new database session using SessionLocal, yields it for use in the endpoint, and ensures that the session is closed after the request is completed. This pattern is used to manage database connections efficiently and avoid resource leaks.
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # Home
# @app.get("/")
# def home():
#     return {
#         "message": "Blog API"
#     }

# # Create Blog
# @app.post("/blogs", response_model=schemas.BlogResponse)
# def create_blog(blog:schemas.BlogCreate, db:Session = Depends(get_db)):
#     new_blog = models.Blog(
#         title = blog.title,
#         content = blog.content
#     )
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# # Read all Blogs
# @app.get("/blogs", response_model=list[schemas.BlogResponse])
# def get_blogs(db: Session = Depends(get_db)):
#     return db.query(models.Blog).all()

# # Read one Blog
# @app.get("/blogs/{id}", response_model=schemas.BlogResponse)
# def get_blog(id:int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()

#     if not blog:
#         raise HTTPException(
#             status_code=404,
#             detail="not found"
#         )

#     return blog

# # Update Blog API
# @app.put("/blogs/{id}", response_model=schemas.BlogResponse)
# def update_blog(id:int, blog:schemas.BlogCreate, db: Session = Depends(get_db)):
#     existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()

#     if not existing_blog:
#         raise HTTPException(
#             status_code=404,
#             detail="not found"
#         )

#     existing_blog.title, existing_blog.content = blog.title, blog.content

#     db.commit()

#     return existing_blog

# # Delete Blog API
# @app.delete("/blogs/{id}")
# def delete_blog(id:int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)

#     if not blog.first():
#         raise HTTPException(
#             status_code=404,
#             detail="not found"
#         )

#     blog.delete()
#     db.commit()

#     return {
#         "message": "blog deleted successfully"
#     }

from fastapi import FastAPI, HTTPException, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from schemas import BlogsCreate, BlogsResponse
from models import Blog

app = FastAPI()

# Get Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home page
@app.get("/")
def home():
    return {
        "message": "Hello Tinksss"
    }

# Create Blog API
@app.post("/blogs", response_model=BlogsResponse)
def create_blogs(blog: BlogsCreate, db: Session = Depends(get_db)):
    new_blog = Blog(
        title = blog.title,
        content = blog.content
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

# Read all Blogs API
@app.get("/blogs", response_model=list[BlogsResponse])
def get_blogs(db:Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

# Read one Blog API
@app.get("/blogs/{id}")
def get_blog(id:str, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    return blog

# Update Blog API
@app.put("/blogs/{id}")
def update_blog(id: int, blog: BlogsCreate, db:Session = Depends(get_db)):
    current_blog = db.query(Blog).filter(Blog.id == id).first()

    if not current_blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    current_blog.title = blog.title
    current_blog.content = blog.content

    db.commit()
    db.refresh(current_blog)

    return {
        "message" : "Blog updated successfully",
        "blog" : current_blog
    }

@app.delete("/blogs/{id}")
def delete_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )
    
    blog.delete()
    db.commit()

    return {
        "message": "Blog deleted successfully"
    }