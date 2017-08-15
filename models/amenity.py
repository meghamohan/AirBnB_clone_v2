#!/usr/bin/python3
"""
Amenity Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String

class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""
    if os.getenv('HBNB_TYPE_STORAGE') is not "db":
        name = ''
    else:
        ___tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("PlaceAmenity", cascade="all,delete", backref="amenities")

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
