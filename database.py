# # Database connection and session management for SQLAlchemy with PostgreSQL.

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql+psycopg2://fastapi_user:cricketkar1@localhost:5432/blogdb" # Database URL for PostgreSQL connection.

# engine = create_engine(DATABASE_URL) # Create a SQLAlchemy engine for connecting to the PostgreSQL database. 

# SessionLocal = sessionmaker(bind=engine) # Create a session factory for creating new database sessions. Use SessionLocal() to create a new session when needed. It is used to interact with the database in a thread-safe manner.

# Base = declarative_base() # Create a base class for declarative class definitions, which will be used to define the database models.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://fastapi_user:cricketkar1@localhost:5432/blogdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()