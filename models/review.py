#!/usr/bin/python3
"""
Review Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String

class Review(BaseModel, Base):
    """Review class handles all application reviews"""
    if os.environ['HBNB_TYPE_STORAGE'] is not "db":
        place_id = ''
        user_id = ''
        text = ''
    else:
         ___tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey('places.id')
        user_id = Column(String(60), nullable=False, ForeignKey('users.id')

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
