#!/usr/bin/python3
"""
   unittest suite for model/state.py
"""
import unittest
import sys
import os
import json
from models import storage
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
from io import StringIO


class TestStateClass(unittest.TestCase):
    """class TestStateClass"""

    def test_state_type(self):
        """tests state instance is created"""
        s = State()
        self.assertEqual(type(State()), type(s))

    def test_name_default(self):
        """tests default value of name attr"""
        s = State()
        self.assertEqual("", s.name)

    def test_id(self):
        """id attr test"""
        s = State()
        self.assertEqual(str, type(s.id))

    def test_created_at(self):
        """created_at attr test"""
        s = State()
        self.assertEqual(datetime, type(s.created_at))

    def test_updated_at(self):
        """created_at attr test"""
        s = State()
        self.assertEqual(datetime, type(s.updated_at))

    def test_created_and_updated_at_init(self):
        """created_at and updated_at attrs initialized
        to current datetime test"""
        s = State()
        self.assertEqual(s.created_at, s.updated_at)

    def test_save_updated_at(self):
        """save method changing updated_at attr to current datetime test"""
        s = State()
        prev_updated_at = s.updated_at
        s.save()
        self.assertNotEqual(prev_updated_at, s.updated_at)

    def test_save_created_at(self):
        """save method changing updated_at attr to current datetime test
        but leaves created_at unchanged"""
        s = State()
        prev_created_at = s.created_at
        s.save()
        self.assertEqual(prev_created_at, s.created_at)

    def test_str_method(self):
        """test __str__ represetation in stdout"""
        s = State()
        try:
            stdout, sys.stdout = sys.stdout, StringIO()
            print(s)
            output = sys.stdout.getvalue().strip()
            expect = '[{}] ({}) {}'.format(type(s).__name__, s.id, s.__dict__)
            assert output == expect
        finally:
            sys.stdout = stdout

    def test_class_name(self):
        """test __class__ key in dictionary"""
        s = State()
        state_dictionary = s.to_dict()
        self.assertIn('__class__', state_dictionary)

    def test_class_name_user(self):
        """test __class__ key in dictionary value is State"""
        s = State()
        state_dictionary = s.to_dict()
        self.assertEqual('State', state_dictionary['__class__'])

    def test_to_dict_id_str(self):
        """test type of 'id' value is a str"""
        s = State()
        s_dictionary = s.to_dict()
        self.assertEqual(str, type(s_dictionary['id']))

    def test_to_dict_updated_at(self):
        """test 'updated_at' is in dictionary returned by to_dict method"""
        s = State()
        s_dictionary = s.to_dict()
        self.assertIn('updated_at', s_dictionary)

    def test_to_dict_updated_at_str(self):
        """test type of 'updated_at' value is a str"""
        s = State()
        s_dictionary = s.to_dict()
        self.assertEqual(str, type(s_dictionary['updated_at']))

    def test_to_dict_created_at(self):
        """test 'created_at' is in dictionary returned by to_dict method"""
        s = State()
        s_dictionary = s.to_dict()
        self.assertIn('created_at', s_dictionary)

    def test_to_dict_created_at_str(self):
        """test type of 'created_at' value is a str"""
        s = State()
        s_dictionary = s.to_dict()
        self.assertEqual(str, type(s_dictionary['created_at']))

    def test_dict_to_instance(self):
        """test dict -> instance"""
        s = State()
        s_dictionary = s.to_dict()
        s2 = State(**s_dictionary)
        self.assertEqual(type(s), type(s2))

    def test_dict_to_id_attr(self):
        """test dict -> instance's id attr"""
        s = State()
        s_dictionary = s.to_dict()
        s2 = State(**s_dictionary)
        self.assertEqual(s.id, s2.id)

    def test_dict_to_id_attr_type(self):
        """test dict -> instance's id attr"""
        s = State()
        s_dictionary = s.to_dict()
        s2 = State(**s_dictionary)
        self.assertEqual(str, type(s2.id))

    def test_dict_to_updated_at_attr(self):
        """test dict -> instance's updated_at attr"""
        s = State()
        s_dictionary = s.to_dict()
        s2 = State(**s_dictionary)
        self.assertEqual(s.updated_at, s2.updated_at)

    def test_dict_to_updated_at_attr_type(self):
        """test dict -> instance's updated_at attr type"""
        s = State()
        s_dictionary = s.to_dict()
        s2 = State(**s_dictionary)
        self.assertEqual(type(datetime.now()), type(s2.updated_at))

    def test_dict_to_created_at_attr(self):
        """test dict -> instance's created_at attr"""
        s = State()
        s_dictionary = s.to_dict()
        s2 = State(**s_dictionary)
        self.assertEqual(s.created_at, s2.created_at)

    def test_dict_to_created_at_attr_type(self):
        """test dict -> instance's created_at attr type"""
        s = State()
        s_dictionary = s.to_dict()
        s2 = State(**s_dictionary)
        self.assertEqual(type(datetime.now()), type(s2.created_at))
