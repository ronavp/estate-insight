"""Database models and connection setup for the Real Estate project."""
import os
from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv

# Load all environment variables from .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)

Base = declarative_base()

class Property(Base):
    """Model representing a property listing."""
    __tablename__ = 'properties'
    
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String(255), nullable=False)
    # Metres Square
    size = Column(Float, nullable=False) 
    # Residential or Commercial
    type = Column(String(50), nullable=False)  
    price = Column(Float, nullable=False)
    # Sold, For Sael or For Lease
    status = Column(String(50), nullable=False)  #