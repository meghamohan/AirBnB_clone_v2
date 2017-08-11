#!/usr/bin/python3
"""
City Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel, Base):
    """City class handles all application cities"""

    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'),
                          nullable=False)
        places = relationship("Place", cascade="all,delete",
                              backref="cities")
    else:
        state_id = ''
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
