#!/usr/bin/python3
"""
   unittest suite for model/city.py
"""
import unittest
import sys
import os
import json
from models import storage
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from io import StringIO


class TestCityClass(unittest.TestCase):
    """class TestCityClass"""

    def test_city_type(self):
        """tests city instance is created"""
        c = City()
        self.assertEqual(type(City()), type(c))

    def test_state_id_default(self):
        """tests default value of state_id attr"""
        c = City()
        self.assertEqual("", c.state_id)

    def test_name_default(self):
        """tests default value of name attr"""
        c = City()
        self.assertEqual("", c.name)

    def test_id(self):
        """id attr test"""
        c = City()
        self.assertEqual(str, type(c.id))

    def test_created_at(self):
        """created_at attr test"""
        c = City()
        self.assertEqual(datetime, type(c.created_at))

    def test_updated_at(self):
        """created_at attr test"""
        c = City()
        self.assertEqual(datetime, type(c.updated_at))

    def test_created_and_updated_at_init(self):
        """created_at and updated_at attrs initialized
        to current datetime test"""
        c = City()
        self.assertEqual(c.created_at, c.updated_at)

    def test_save_updated_at(self):
        """save method changing updated_at attr to current datetime test"""
        c = City()
        prev_updated_at = c.updated_at
        c.save()
        self.assertNotEqual(prev_updated_at, c.updated_at)

    def test_save_created_at(self):
        """save method changing updated_at attr to current datetime test
        but leaves created_at unchanged"""
        c = City()
        prev_created_at = c.created_at
        c.save()
        self.assertEqual(prev_created_at, c.created_at)

    def test_str_method(self):
        """test __str__ represetation in stdout"""
        c = City()
        try:
            stdout, sys.stdout = sys.stdout, StringIO()
            print(c)
            output = sys.stdout.getvalue().strip()
            expect = '[{}] ({}) {}'.format(type(c).__name__, c.id, c.__dict__)
            assert output == expect
        finally:
            sys.stdout = stdout

    def test_class_name(self):
        """test __class__ key in dictionary"""
        c = City()
        c_dictionary = c.to_dict()
        self.assertIn('__class__', c_dictionary)

    def test_class_name_user(self):
        """test __class__ key in dictionary value is State"""
        c = City()
        c_dictionary = c.to_dict()
        self.assertEqual('City', c_dictionary['__class__'])

    def test_to_dict_id_str(self):
        """test type of 'id' value is a str"""
        c = City()
        c_dictionary = c.to_dict()
        self.assertEqual(str, type(c_dictionary['id']))

    def test_to_dict_updated_at(self):
        """test 'updated_at' is in dictionary returned by to_dict method"""
        c = City()
        c_dictionary = c.to_dict()
        self.assertIn('updated_at', c_dictionary)

    def test_to_dict_updated_at_str(self):
        """test type of 'updated_at' value is a str"""
        c = City()
        c_dictionary = c.to_dict()
        self.assertEqual(str, type(c_dictionary['updated_at']))

    def test_to_dict_created_at(self):
        """test 'created_at' is in dictionary returned by to_dict method"""
        c = City()
        c_dictionary = c.to_dict()
        self.assertIn('created_at', c_dictionary)

    def test_to_dict_created_at_str(self):
        """test type of 'created_at' value is a str"""
        c = City()
        c_dictionary = c.to_dict()
        self.assertEqual(str, type(c_dictionary['created_at']))

    def test_dict_to_instance(self):
        """test dict -> instance"""
        c = City()
        c_dictionary = c.to_dict()
        c2 = City(**c_dictionary)
        self.assertEqual(type(c), type(c2))

    def test_dict_to_id_attr(self):
        """test dict -> instance's id attr"""
        c = City()
        c_dictionary = c.to_dict()
        c2 = City(**c_dictionary)
        self.assertEqual(c.id, c2.id)

    def test_dict_to_id_attr_type(self):
        """test dict -> instance's id attr"""
        c = City()
        c_dictionary = c.to_dict()
        c2 = City(**c_dictionary)
        self.assertEqual(str, type(c2.id))

    def test_dict_to_updated_at_attr(self):
        """test dict -> instance's updated_at attr"""
        c = City()
        c_dictionary = c.to_dict()
        c2 = City(**c_dictionary)
        self.assertEqual(c.updated_at, c2.updated_at)

    def test_dict_to_updated_at_attr_type(self):
        """test dict -> instance's updated_at attr type"""
        c = City()
        c_dictionary = c.to_dict()
        c2 = City(**c_dictionary)
        self.assertEqual(type(datetime.now()), type(c2.updated_at))

    def test_dict_to_created_at_attr(self):
        """test dict -> instance's created_at attr"""
        c = City()
        c_dictionary = c.to_dict()
        c2 = City(**c_dictionary)
        self.assertEqual(c.created_at, c2.created_at)

    def test_dict_to_created_at_attr_type(self):
        """test dict -> instance's created_at attr type"""
        c = City()
        c_dictionary = c.to_dict()
        c2 = City(**c_dictionary)
        self.assertEqual(type(datetime.now()), type(c2.created_at))
