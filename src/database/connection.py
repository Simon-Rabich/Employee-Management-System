from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from common.configurations.config import DATABASE_URL

# Create the SQLAlchemy engine using the DATABASE_URL from config.py
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()


# Dependency that provides a database session to be used in API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
