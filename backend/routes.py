"""Intialisation"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/properties")
def get_properties():
    """Gets the properties in the db"""
    return {"properties:" "List of properties will be displayed here"}