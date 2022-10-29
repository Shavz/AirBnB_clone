#!/usr/bin/python3
"""
   unittest suite for model/user.py
"""
import unittest
import sys
import os
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from io import StringIO


class TestUserClass(unittest.TestCase):
    """class TestUserClass"""

    def test_user_type(self):
        """tests user instance is created"""
        u = User()
        self.assertEqual(type(User()), type(u))

    def test_email_default(self):
        """tests default value of email attr"""
        u = User()
        self.assertEqual("", u.email)

    def test_password_default(self):
        """tests default value of password attr"""
        u = User()
        self.assertEqual("", u.password)

    def test_first_name_default(self):
        """tests default value of first_name attr"""
        u = User()
        self.assertEqual("", u.first_name)

    def test_last_name_default(self):
        """tests default value of last_name attr"""
        u = User()
        self.assertEqual("", u.last_name)

    def test_id(self):
        """id attr test"""
        u = User()
        self.assertEqual(str, type(u.id))

    def test_created_at(self):
        """created_at attr test"""
        u = User()
        self.assertEqual(datetime, type(u.created_at))

    def test_updated_at(self):
        """created_at attr test"""
        u = User()
        self.assertEqual(datetime, type(u.updated_at))

    def test_created_and_updated_at_init(self):
        """created_at and updated_at attrs initialized
        to current datetime test"""
        u = User()
        self.assertEqual(u.created_at, u.updated_at)

    def test_save_updated_at(self):
        """save method changing updated_at attr to current datetime test"""
        u = User()
        prev_updated_at = u.updated_at
        u.save()
        self.assertNotEqual(prev_updated_at, u.updated_at)

    def test_save_created_at(self):
        """save method changing updated_at attr to current datetime test
        but leaves created_at unchanged"""
        u = User()
        prev_created_at = u.created_at
        u.save()
        self.assertEqual(prev_created_at, u.created_at)

    def test_str_method(self):
        """test __str__ represetation in stdout"""
        u = User()
        try:
            stdout, sys.stdout = sys.stdout, StringIO()
            print(u)
            output = sys.stdout.getvalue().strip()
            expect = '[{}] ({}) {}'.format(type(u).__name__, u.id, u.__dict__)
            assert output == expect
        finally:
            sys.stdout = stdout

    def test_class_name(self):
        """test __class__ key in dictionary"""
        u = User()
        user_dictionary = u.to_dict()
        self.assertIn('__class__', user_dictionary)

    def test_class_name_user(self):
        """test __class__ key in dictionary value is User"""
        u = User()
        user_dictionary = u.to_dict()
        self.assertEqual('User', user_dictionary['__class__'])

    def test_to_dict_id_str(self):
        """test type of 'id' value is a str"""
        u = User()
        u_dictionary = u.to_dict()
        self.assertEqual(str, type(u_dictionary['id']))

    def test_to_dict_updated_at(self):
        """test 'updated_at' is in dictionary returned by to_dict method"""
        u = User()
        u_dictionary = u.to_dict()
        self.assertIn('updated_at', u_dictionary)

    def test_to_dict_updated_at_str(self):
        """test type of 'updated_at' value is a str"""
        u = User()
        u_dictionary = u.to_dict()
        self.assertEqual(str, type(u_dictionary['updated_at']))

    def test_to_dict_created_at(self):
        """test 'created_at' is in dictionary returned by to_dict method"""
        u = User()
        u_dictionary = u.to_dict()
        self.assertIn('created_at', u_dictionary)

    def test_to_dict_created_at_str(self):
        """test type of 'created_at' value is a str"""
        u = User()
        u_dictionary = u.to_dict()
        self.assertEqual(str, type(u_dictionary['created_at']))

    def test_dict_to_instance(self):
        """test dict -> instance"""
        u = User()
        u_dictionary = u.to_dict()
        u2 = User(**u_dictionary)
        self.assertEqual(type(u), type(u2))

    def test_dict_to_id_attr(self):
        """test dict -> instance's id attr"""
        u = User()
        u_dictionary = u.to_dict()
        u2 = User(**u_dictionary)
        self.assertEqual(u.id, u2.id)

    def test_dict_to_id_attr_type(self):
        """test dict -> instance's id attr"""
        u = User()
        u_dictionary = u.to_dict()
        u2 = User(**u_dictionary)
        self.assertEqual(str, type(u2.id))

    def test_dict_to_updated_at_attr(self):
        """test dict -> instance's updated_at attr"""
        u = User()
        u_dictionary = u.to_dict()
        u2 = User(**u_dictionary)
        self.assertEqual(u.updated_at, u2.updated_at)

    def test_dict_to_updated_at_attr_type(self):
        """test dict -> instance's updated_at attr type"""
        u = User()
        u_dictionary = u.to_dict()
        u2 = User(**u_dictionary)
        self.assertEqual(type(datetime.now()), type(u2.updated_at))

    def test_dict_to_created_at_attr(self):
        """test dict -> instance's created_at attr"""
        u = User()
        u_dictionary = u.to_dict()
        u2 = User(**u_dictionary)
        self.assertEqual(u.created_at, u2.created_at)

    def test_dict_to_created_at_attr_type(self):
        """test dict -> instance's created_at attr type"""
        u = User()
        u_dictionary = u.to_dict()
        u2 = User(**u_dictionary)
        self.assertEqual(type(datetime.now()), type(u2.created_at))
