from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import DATABASE_URL

<<<<<<< HEAD
# Create the SQLAlchemy engine using the DATABASE_URL from config.py
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

# Dependency that provides a database session to be used in API routes
=======
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

>>>>>>> f0ae657d6e8455067a87cef92b8ffd1a79880ab7
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
