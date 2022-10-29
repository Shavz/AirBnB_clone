#!/usr/bin/python3
"""
   unittest suite for model/amenity.py
"""
import unittest
import sys
import os
import json
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
from io import StringIO


class TestAmenityClass(unittest.TestCase):
    """class TestAmenityClass"""

    def test_amenity_type(self):
        """tests amenity instance is created"""
        a = Amenity()
        self.assertEqual(type(Amenity()), type(a))

    def test_name_default(self):
        """tests default value of name attr"""
        a = Amenity()
        self.assertEqual("", a.name)

    def test_id(self):
        """id attr test"""
        a = Amenity()
        self.assertEqual(str, type(a.id))

    def test_created_at(self):
        """created_at attr test"""
        a = Amenity()
        self.assertEqual(datetime, type(a.created_at))

    def test_updated_at(self):
        """created_at attr test"""
        a = Amenity()
        self.assertEqual(datetime, type(a.updated_at))

    def test_created_and_updated_at_init(self):
        """created_at and updated_at attrs initialized
        to current datetime test"""
        a = Amenity()
        self.assertEqual(a.created_at, a.updated_at)

    def test_save_updated_at(self):
        """save method changing updated_at attr to current datetime test"""
        a = Amenity()
        prev_updated_at = a.updated_at
        a.save()
        self.assertNotEqual(prev_updated_at, a.updated_at)

    def test_save_created_at(self):
        """save method changing updated_at attr to current datetime test
        but leaves created_at unchanged"""
        a = Amenity()
        prev_created_at = a.created_at
        a.save()
        self.assertEqual(prev_created_at, a.created_at)

    def test_str_method(self):
        """test __str__ represetation in stdout"""
        a = Amenity()
        try:
            stdout, sys.stdout = sys.stdout, StringIO()
            print(a)
            output = sys.stdout.getvalue().strip()
            expect = '[{}] ({}) {}'.format(type(a).__name__, a.id, a.__dict__)
            assert output == expect
        finally:
            sys.stdout = stdout

    def test_class_name(self):
        """test __class__ key in dictionary"""
        a = Amenity()
        a_dictionary = a.to_dict()
        self.assertIn('__class__', a_dictionary)

    def test_class_name_user(self):
        """test __class__ key in dictionary value is State"""
        a = Amenity()
        a_dictionary = a.to_dict()
        self.assertEqual('Amenity', a_dictionary['__class__'])

    def test_to_dict_id_str(self):
        """test type of 'id' value is a str"""
        a = Amenity()
        a_dictionary = a.to_dict()
        self.assertEqual(str, type(a_dictionary['id']))

    def test_to_dict_updated_at(self):
        """test 'updated_at' is in dictionary returned by to_dict method"""
        a = Amenity()
        a_dictionary = a.to_dict()
        self.assertIn('updated_at', a_dictionary)

    def test_to_dict_updated_at_str(self):
        """test type of 'updated_at' value is a str"""
        a = Amenity()
        a_dictionary = a.to_dict()
        self.assertEqual(str, type(a_dictionary['updated_at']))

    def test_to_dict_created_at(self):
        """test 'created_at' is in dictionary returned by to_dict method"""
        a = Amenity()
        a_dictionary = a.to_dict()
        self.assertIn('created_at', a_dictionary)

    def test_to_dict_created_at_str(self):
        """test type of 'created_at' value is a str"""
        a = Amenity()
        a_dictionary = a.to_dict()
        self.assertEqual(str, type(a_dictionary['created_at']))

    def test_dict_to_instance(self):
        """test dict -> instance"""
        a = Amenity()
        a_dictionary = a.to_dict()
        a2 = Amenity(**a_dictionary)
        self.assertEqual(type(a), type(a2))

    def test_dict_to_id_attr(self):
        """test dict -> instance's id attr"""
        a = Amenity()
        a_dictionary = a.to_dict()
        a2 = Amenity(**a_dictionary)
        self.assertEqual(a.id, a2.id)

    def test_dict_to_id_attr_type(self):
        """test dict -> instance's id attr"""
        a = Amenity()
        a_dictionary = a.to_dict()
        a2 = Amenity(**a_dictionary)
        self.assertEqual(str, type(a2.id))

    def test_dict_to_updated_at_attr(self):
        """test dict -> instance's updated_at attr"""
        a = Amenity()
        a_dictionary = a.to_dict()
        a2 = Amenity(**a_dictionary)
        self.assertEqual(a.updated_at, a2.updated_at)

    def test_dict_to_updated_at_attr_type(self):
        """test dict -> instance's updated_at attr type"""
        a = Amenity()
        a_dictionary = a.to_dict()
        a2 = Amenity(**a_dictionary)
        self.assertEqual(type(datetime.now()), type(a2.updated_at))

    def test_dict_to_created_at_attr(self):
        """test dict -> instance's created_at attr"""
        a = Amenity()
        a_dictionary = a.to_dict()
        a2 = Amenity(**a_dictionary)
        self.assertEqual(a.created_at, a2.created_at)

    def test_dict_to_created_at_attr_type(self):
        """test dict -> instance's created_at attr type"""
        a = Amenity()
        a_dictionary = a.to_dict()
        a2 = Amenity(**a_dictionary)
        self.assertEqual(type(datetime.now()), type(a2.created_at))
