from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from schemas import BlogsCreate, BlogsResponse, UserCreate
from models import Blog, User, Base

from auth import create_token, verify_token

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Get Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create User API
@app.post("/signup")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username = user.username,
        password = user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "access_token" : create_token({"sub":user.username}),
        "token_type" : "bearer"
    }

# Login API
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    current_user = db.query(User).filter(User.username == form_data.username, User.password == form_data.password).first()

    if not current_user:
        raise HTTPException(
            status_code = 401,
            detail="user not found or invalid credentials"
        )
    return {
        "access_token" : create_token({"sub":current_user.username}),
        "token_type" : "bearer"
    }

# Home page
@app.get("/")
def home():
    return {
        "message": "Hello Tinksss"
    }

# Create Blog API (Protected)
@app.post("/blogs", response_model=BlogsResponse)
def create_blogs(blog: BlogsCreate, db: Session = Depends(get_db), user = Depends(verify_token)):
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

# Update Blog API (Protected)
@app.put("/blogs/{id}")
def update_blog(id: int, blog: BlogsCreate, db:Session = Depends(get_db), user = Depends(verify_token)):
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

# Delete a Blog API
@app.delete("/blogs/{id}")
def delete_blog(id:int, db:Session = Depends(get_db), user = Depends
(verify_token)):
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