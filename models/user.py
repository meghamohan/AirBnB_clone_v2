#!/usr/bin/python3
"""
User Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    """User class handles all application users"""
    if os.environ['HBNB_TYPE_STORAGE'] is not "db":
        email = ''
        password = ''
        first_name = ''
        last_name = ''
    else:
         ___tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)  
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all,delete", backref="user")
        reviews = relationship("Review", cascade="all,delete", backref="user")

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
