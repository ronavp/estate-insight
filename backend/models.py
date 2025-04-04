"""Intialisation"""
import os
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv

# Load all environment variables from .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine and session 
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base