#!/usr/bin/python3
"""
City Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class City(BaseModel, Base):
    """City class handles all application cities"""

    if os.environ['HBNB_TYPE_STORAGE'] is not "db":    
        state_id = ''
        name = ''
    else:
         ___tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
        places = relationship("Place", cascade="all,delete", backref="cities")

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
