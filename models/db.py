from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# using SQLite for simplicity; database file will be flood.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./flood.db"
# echo=True for debugging, can be turned off
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# dependency for FastAPI

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
