#!/usr/bin/python3
"""
Place Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class Place(BaseModel, Base):
    """Place class handles all application places"""

    if os.environ['HBNB_TYPE_STORAGE'] is not "db":
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = ['', '']
    else:
        metadata = Base.metadata
        place_amenity = Table("place_amenity", metadata,
                              Column('place_id', String(60),\
                               nullable=False, ForeignKey("places.id")),
                              Column('amenity_id', String(60),\
                               nullable=False, ForeignKey("amenities.id"))
                            )

        ___tablename__ = 'places'
        city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
        user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
        reviews = relationship("Review", cascade="all,delete", backref="place")

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)
