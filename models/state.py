#!/usr/bin/python3
"""
State Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
from datetime import datetime


class State(BaseModel, Base):
    """State class handles all application states"""
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete,delete-orphan",
                              backref="state")
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)

    if os.environ.get('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """ return all city objects in a State"""
            cities = models.storage.all("City").values()
            result = []
            for city in cities:
                if city.state_id == self.id:
                    result.append(city)
            return result
