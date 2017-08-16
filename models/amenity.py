#!/usr/bin/python3
"""
Amenity Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String

class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("PlaceAmenity", cascade="all,delete", backref="amenities")
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
