"""Intialises the tables for the db"""
from .models import Base, engine  

# Create all tables defined in the model (properties table)
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Estate-Insight Databse tables created successfully")

