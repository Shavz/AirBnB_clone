#!/usr/bin/python3
"""
   unittest suite for model/place.py
"""
import unittest
import sys
import os
import json
from models import storage
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
from io import StringIO


class TestPlaceClass(unittest.TestCase):
    """class TestUserClass"""

    def test_Place_type(self):
        """tests place instance is created"""
        p = Place()
        self.assertEqual(type(Place()), type(p))

    def test_city_id_default(self):
        """tests default value of city_id attr"""
        p = Place()
        self.assertEqual("", p.city_id)

    def test_user_id_default(self):
        """tests default value of user_id attr"""
        p = Place()
        self.assertEqual("", p.user_id)

    def test_name_default(self):
        """tests default value of name attr"""
        p = Place()
        self.assertEqual("", p.name)

    def test_description_default(self):
        """tests default value of description attr"""
        p = Place()
        self.assertEqual("", p.description)

    def test_number_rooms_default(self):
        """tests default value of number_rooms attr"""
        p = Place()
        self.assertEqual(0, p.number_rooms)

    def test_number_bathrooms_default(self):
        """tests default value of number_bathrooms attr"""
        p = Place()
        self.assertEqual(0, p.number_bathrooms)

    def test_max_guest_default(self):
        """tests default value of max_guest attr"""
        p = Place()
        self.assertEqual(0, p.max_guest)

    def test_price_by_night_default(self):
        """tests default value of price_by_night attr"""
        p = Place()
        self.assertEqual(0, p.price_by_night)

    def test_latitude_default(self):
        """tests default value of latitude attr"""
        p = Place()
        self.assertEqual(0.0, p.latitude)

    def test_longitude_default(self):
        """tests default value of longitude attr"""
        p = Place()
        self.assertEqual(0.0, p.longitude)

    def test_amenity_ids_default(self):
        """tests default value of amenity_ids attr"""
        p = Place()
        self.assertEqual([], p.amenity_ids)

    def test_id(self):
        """id attr test"""
        p = Place()
        self.assertEqual(str, type(p.id))

    def test_created_at(self):
        """created_at attr test"""
        p = Place()
        self.assertEqual(datetime, type(p.created_at))

    def test_updated_at(self):
        """created_at attr test"""
        p = Place()
        self.assertEqual(datetime, type(p.updated_at))

    def test_created_and_updated_at_init(self):
        """created_at and updated_at attrs initialized
        to current datetime test"""
        p = Place()
        self.assertEqual(p.created_at, p.updated_at)

    def test_save_updated_at(self):
        """save method changing updated_at attr to current datetime test"""
        p = Place()
        prev_updated_at = p.updated_at
        p.save()
        self.assertNotEqual(prev_updated_at, p.updated_at)

    def test_save_created_at(self):
        """save method changing updated_at attr to current datetime test
        but leaves created_at unchanged"""
        p = Place()
        prev_created_at = p.created_at
        p.save()
        self.assertEqual(prev_created_at, p.created_at)

    def test_str_method(self):
        """test __str__ represetation in stdout"""
        p = Place()
        try:
            stdout, sys.stdout = sys.stdout, StringIO()
            print(p)
            output = sys.stdout.getvalue().strip()
            expect = '[{}] ({}) {}'.format(type(p).__name__, p.id, p.__dict__)
            assert output == expect
        finally:
            sys.stdout = stdout

    def test_class_name(self):
        """test __class__ key in dictionary"""
        p = Place()
        p_dictionary = p.to_dict()
        self.assertIn('__class__', p_dictionary)

    def test_class_name_user(self):
        """test __class__ key in dictionary value is User"""
        p = Place()
        p_dictionary = p.to_dict()
        self.assertEqual('Place', p_dictionary['__class__'])

    def test_to_dict_id_str(self):
        """test type of 'id' value is a str"""
        p = Place()
        p_dictionary = p.to_dict()
        self.assertEqual(str, type(p_dictionary['id']))

    def test_to_dict_updated_at(self):
        """test 'updated_at' is in dictionary returned by to_dict method"""
        p = Place()
        p_dictionary = p.to_dict()
        self.assertIn('updated_at', p_dictionary)

    def test_to_dict_updated_at_str(self):
        """test type of 'updated_at' value is a str"""
        p = Place()
        p_dictionary = p.to_dict()
        self.assertEqual(str, type(p_dictionary['updated_at']))

    def test_to_dict_created_at(self):
        """test 'created_at' is in dictionary returned by to_dict method"""
        p = Place()
        p_dictionary = p.to_dict()
        self.assertIn('created_at', p_dictionary)

    def test_to_dict_created_at_str(self):
        """test type of 'created_at' value is a str"""
        p = Place()
        p_dictionary = p.to_dict()
        self.assertEqual(str, type(p_dictionary['created_at']))

    def test_dict_to_instance(self):
        """test dict -> instance"""
        p = Place()
        p_dictionary = p.to_dict()
        p2 = Place(**p_dictionary)
        self.assertEqual(type(p), type(p2))

    def test_dict_to_id_attr(self):
        """test dict -> instance's id attr"""
        p = Place()
        p_dictionary = p.to_dict()
        p2 = Place(**p_dictionary)
        self.assertEqual(p.id, p2.id)

    def test_dict_to_id_attr_type(self):
        """test dict -> instance's id attr"""
        p = Place()
        p_dictionary = p.to_dict()
        p2 = Place(**p_dictionary)
        self.assertEqual(str, type(p2.id))

    def test_dict_to_updated_at_attr(self):
        """test dict -> instance's updated_at attr"""
        p = Place()
        p_dictionary = p.to_dict()
        p2 = Place(**p_dictionary)
        self.assertEqual(p.updated_at, p2.updated_at)

    def test_dict_to_updated_at_attr_type(self):
        """test dict -> instance's updated_at attr type"""
        p = Place()
        p_dictionary = p.to_dict()
        p2 = Place(**p_dictionary)
        self.assertEqual(type(datetime.now()), type(p2.updated_at))

    def test_dict_to_created_at_attr(self):
        """test dict -> instance's created_at attr"""
        p = Place()
        p_dictionary = p.to_dict()
        p2 = Place(**p_dictionary)
        self.assertEqual(p.created_at, p2.created_at)

    def test_dict_to_created_at_attr_type(self):
        """test dict -> instance's created_at attr type"""
        p = Place()
        p_dictionary = p.to_dict()
        p2 = Place(**p_dictionary)
        self.assertEqual(type(datetime.now()), type(p2.created_at))
