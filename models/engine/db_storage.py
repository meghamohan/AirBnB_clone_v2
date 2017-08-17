#!/usr/bin/python3

import os
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ DB storage """
    __engine = None
    __session = None
    clsDict = {'Amenity': Amenity, 'User': User, 'City': City,
               'Place': Place, 'Review': Review, 'State': State}

    def __init__(self):
        """ init """
        usr = os.environ.get('HBNB_MYSQL_USER')
        passwd = os.environ.get('HBNB_MYSQL_PWD')
        database = os.environ.get('HBNB_MYSQL_DB')
        hostname = os.environ.get('HBNB_MYSQL_HOST')
        port = 3306

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                                                                   usr,
                                                                   passwd,
                                                                   hostname,
                                                                   port,
                                                                   database))
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all """
        objDicts = {}
        if cls is None:
            for k, v in self.clsDict.items():
                for allObjs in self.__session.query(v):
                    objDicts[allObjs.id] = allObjs
        else:
            for allObjs in self.__session.query(self.clsDict[cls]):
                objDicts[allObjs.id] = allObjs
        return objDicts

    def new(self, obj):
        """ new """
        self.__session.add(obj)

    def save(self):
        """ save """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ all classes who inherit from Base must be imported"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
