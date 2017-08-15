#!/usr/bin/python3
"""
State Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """State class handles all application states"""
    
    if os.environ['HBNB_TYPE_STORAGE'] is not "db":
        name = ''
    else:
        ___tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete", backref="state")

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
