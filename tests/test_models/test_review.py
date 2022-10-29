#!/usr/bin/python3
"""
   unittest suite for model/review.py
"""
import unittest
import sys
import os
import json
from models import storage
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
from io import StringIO


class TestReviewClass(unittest.TestCase):
    """class TestReviewClass"""

    def test_review_type(self):
        """tests review instance is created"""
        r = Review()
        self.assertEqual(type(Review()), type(r))

    def test_place_id_default(self):
        """tests default value of place_id attr"""
        r = Review()
        self.assertEqual("", r.place_id)

    def test_user_id_default(self):
        """tests default value of user_id attr"""
        r = Review()
        self.assertEqual("", r.user_id)

    def test_text_default(self):
        """tests default value of text attr"""
        r = Review()
        self.assertEqual("", r.text)

    def test_id(self):
        """id attr test"""
        r = Review()
        self.assertEqual(str, type(r.id))

    def test_created_at(self):
        """created_at attr test"""
        r = Review()
        self.assertEqual(datetime, type(r.created_at))

    def test_updated_at(self):
        """created_at attr test"""
        r = Review()
        self.assertEqual(datetime, type(r.updated_at))

    def test_created_and_updated_at_init(self):
        """created_at and updated_at attrs initialized
        to current datetime test"""
        r = Review()
        self.assertEqual(r.created_at, r.updated_at)

    def test_save_updated_at(self):
        """save method changing updated_at attr to current datetime test"""
        r = Review()
        prev_updated_at = r.updated_at
        r.save()
        self.assertNotEqual(prev_updated_at, r.updated_at)

    def test_save_created_at(self):
        """save method changing updated_at attr to current datetime test
        but leaves created_at unchanged"""
        r = Review()
        prev_created_at = r.created_at
        r.save()
        self.assertEqual(prev_created_at, r.created_at)

    def test_str_method(self):
        """test __str__ represetation in stdout"""
        r = Review()
        try:
            stdout, sys.stdout = sys.stdout, StringIO()
            print(r)
            output = sys.stdout.getvalue().strip()
            expect = '[{}] ({}) {}'.format(type(r).__name__, r.id, r.__dict__)
            assert output == expect
        finally:
            sys.stdout = stdout

    def test_class_name(self):
        """test __class__ key in dictionary"""
        r = Review()
        r_dictionary = r.to_dict()
        self.assertIn('__class__', r_dictionary)

    def test_class_name_review(self):
        """test __class__ key in dictionary value is Review"""
        r = Review()
        r_dictionary = r.to_dict()
        self.assertEqual('Review', r_dictionary['__class__'])

    def test_to_dict_id_str(self):
        """test type of 'id' value is a str"""
        r = Review()
        r_dictionary = r.to_dict()
        self.assertEqual(str, type(r_dictionary['id']))

    def test_to_dict_updated_at(self):
        """test 'updated_at' is in dictionary returned by to_dict method"""
        r = Review()
        r_dictionary = r.to_dict()
        self.assertIn('updated_at', r_dictionary)

    def test_to_dict_updated_at_str(self):
        """test type of 'updated_at' value is a str"""
        r = Review()
        r_dictionary = r.to_dict()
        self.assertEqual(str, type(r_dictionary['updated_at']))

    def test_to_dict_created_at(self):
        """test 'created_at' is in dictionary returned by to_dict method"""
        r = Review()
        r_dictionary = r.to_dict()
        self.assertIn('created_at', r_dictionary)

    def test_to_dict_created_at_str(self):
        """test type of 'created_at' value is a str"""
        r = Review()
        r_dictionary = r.to_dict()
        self.assertEqual(str, type(r_dictionary['created_at']))

    def test_dict_to_instance(self):
        """test dict -> instance"""
        r = Review()
        r_dictionary = r.to_dict()
        r2 = Review(**r_dictionary)
        self.assertEqual(type(r), type(r2))

    def test_dict_to_id_attr(self):
        """test dict -> instance's id attr"""
        r = Review()
        r_dictionary = r.to_dict()
        r2 = Review(**r_dictionary)
        self.assertEqual(r.id, r2.id)

    def test_dict_to_id_attr_type(self):
        """test dict -> instance's id attr"""
        r = Review()
        r_dictionary = r.to_dict()
        r2 = Review(**r_dictionary)
        self.assertEqual(str, type(r2.id))

    def test_dict_to_updated_at_attr(self):
        """test dict -> instance's updated_at attr"""
        r = Review()
        r_dictionary = r.to_dict()
        r2 = Review(**r_dictionary)
        self.assertEqual(r.updated_at, r2.updated_at)

    def test_dict_to_updated_at_attr_type(self):
        """test dict -> instance's updated_at attr type"""
        r = Review()
        r_dictionary = r.to_dict()
        r2 = Review(**r_dictionary)
        self.assertEqual(type(datetime.now()), type(r2.updated_at))

    def test_dict_to_created_at_attr(self):
        """test dict -> instance's created_at attr"""
        r = Review()
        r_dictionary = r.to_dict()
        r2 = Review(**r_dictionary)
        self.assertEqual(r.created_at, r2.created_at)

    def test_dict_to_created_at_attr_type(self):
        """test dict -> instance's created_at attr type"""
        r = Review()
        r_dictionary = r.to_dict()
        r2 = Review(**r_dictionary)
        self.assertEqual(type(datetime.now()), type(r2.created_at))
