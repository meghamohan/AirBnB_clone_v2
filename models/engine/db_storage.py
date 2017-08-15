#!/usr/bin/python3

import os
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from models import base_model, amenity, city, place, review, state, user

class DBStorage:
    __engine = None
    __session = None
    self.clsDict = {'Amenity' : Amenity, 'User' : User, 'City' : City,\
                     'Place' : Place, 'Review' : Review, 'State' : State}

    def __init__(self):
        usr = os.environ['HBNB_MYSQL_USER']
        passwd = os.environ['HBNB_MYSQL_PWD']
        database = os.environ['HBNB_MYSQL_DB']
        hostname = os.environ['HBNB_MYSQL_HOST']
        port = 3306

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(usr,
                                                                   passwd,
                                                                   hostname,
                                                                   port,
                                                                   database))
        
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if os.environ['HBNB_ENV'] is 'test':
            meta = sqlalchemy.MetaData(self.__engine)
            meta.reflect()
            meta.drop_all()

    def all(self, cls=None):
        objDicts = {}
        if cls is None:
            for k,v in self.clsDict:
                for allObjs in self.__session.query(v):
                    objDicts[allObjs.id] = allObj
        else:
            for allObjs in self.__session.query(cls):
                objDicts[allObjs.id] = allObj   
        return objDicts

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.pop(obj)

    def reload(self):
        """ all classes who inherit from Base must be imported"""
        Base.metadata.create_all(engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
