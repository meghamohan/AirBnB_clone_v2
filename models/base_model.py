#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import json
import models
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os


now = datetime.now
strptime = datetime.strptime
if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """attributes and functions for BaseModel class"""
    """class attributes"""
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    else:
        __abstract__ = True

    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = now()
#            models.storage.new(self)

    def __set_attributes(self, d):
        """converts kwargs values to python class attributes"""
        if 'id' not in d:
            d['id'] = str(uuid4())
        if 'created_at' not in d:
            d['created_at'] = now()
        if not isinstance(d['created_at'], datetime):
            d['created_at'] = strptime(d['created_at'], "%Y-%m-%d %H:%M:%S.%f")
        if 'updated_at' in d:
            if not isinstance(d['updated_at'], datetime):
                d['updated_at'] = strptime(d['updated_at'],
                                           "%Y-%m-%d %H:%M:%S.%f")
        if '__class__' in d:
            d.pop('__class__')
        self.__dict__ = d
#        models.storage.new(self)

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            nada = json.dumps(obj_v)
            return True
        except:
            return False

    def bm_update(self, name, value):
        setattr(self, name, value)
        self.save()

    def save(self):
        """updates attribute updated_at to current time"""
        self.updated_at = now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete()

    def to_json(self):
        """returns json representation of self"""
        bm_dict = {}
        if '_sa_instance_state' in self.__dict__:
            self.__dict__.pop('_sa_instance_state')
        for k, v in (self.__dict__).items():
            if (self.__is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = type(self).__name__
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
