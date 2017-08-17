#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
from models import *
import os
from models.base_model import Base
from models.engine.db_storage import DBStorage


State = state.State
City = city.City
Base = base_model.BaseModel
DBStorage = engine.db_storage.DBStorage
storage = storage

@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', 'skip if environ is not db')
class TestDBStorageDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')


    def test_doc_class(self):
        """... documentation for the class"""
        self.assertTrue(len(DBStorage.__doc__) > 1)

    def test_doc_all(self):
        """... documentation for all function"""
        self.assertTrue(len(DBStorage.all.__doc__) > 1)

    def test_doc_new(self):
        """... documentation for new function"""
        self.assertTrue(len(DBStorage.new.__doc__) > 1)

    def test_doc_save(self):
        """... documentation for save function"""
        self.assertTrue(len(DBStorage.save.__doc__) > 1)

    def test_doc_reload(self):
        """... documentation for reload function"""
        self.assertTrue(len(DBStorage.reload.__doc__) > 1)

    def test_doc_delete(self):
        """... documentation for delete function"""
        self.assertTrue(len(DBStorage.delete.__doc__) > 1)

