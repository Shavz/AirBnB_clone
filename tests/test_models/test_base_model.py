#!/usr/bin/python3
"""
   unittest suite for model/base_model.py
"""
import unittest
import sys
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO


class TestBaseModel(unittest.TestCase):
    """class TestBaseClass"""

    def test_id(self):
        """id attr test"""
        model = BaseModel()
        self.assertEqual(str, type(model.id))

    def test_created_at(self):
        """created_at attr test"""
        model = BaseModel()
        self.assertEqual(datetime, type(model.created_at))

    def test_updated_at(self):
        """created_at attr test"""
        model = BaseModel()
        self.assertEqual(datetime, type(model.updated_at))

    def test_created_and_updated_at_init(self):
        """created_at and updated_at attrs initialized
        to current datetime test"""
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    def test_save_updated_at(self):
        """save method changing updated_at attr to current datetime test"""
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(prev_updated_at, model.updated_at)

    def test_save_created_at(self):
        """save method changing updated_at attr to current datetime test
        but leaves created_at unchanged"""
        model = BaseModel()
        prev_created_at = model.created_at
        model.save()
        self.assertEqual(prev_created_at, model.created_at)

    def test_str_method(self):
        """test __str__ represetation in stdout"""
        m = BaseModel()
        try:
            stdout, sys.stdout = sys.stdout, StringIO()
            print(m)
            output = sys.stdout.getvalue().strip()
            expect = '[{}] ({}) {}'.format(type(m).__name__, m.id, m.__dict__)
            assert output == expect
        finally:
            sys.stdout = stdout

    def test_to_dict_type(self):
        """test to_dict returns dictionary"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        self.assertEqual(dict, type(model_dictionary))

    def test_to_dict_class(self):
        """test to_dict adds '__class__' to dictionary"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        self.assertIn('__class__', model_dictionary)

    def test_to_dict_id(self):
        """test 'id' is in dictionary returned by to_dict method"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        self.assertIn('id', model_dictionary)

    def test_to_dict_id_str(self):
        """test type of 'id' value is a str"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        self.assertEqual(str, type(model_dictionary['id']))

    def test_to_dict_updated_at(self):
        """test 'updated_at' is in dictionary returned by to_dict method"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        self.assertIn('updated_at', model_dictionary)

    def test_to_dict_updated_at_str(self):
        """test type of 'updated_at' value is a str"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        self.assertEqual(str, type(model_dictionary['updated_at']))

    def test_to_dict_created_at(self):
        """test 'created_at' is in dictionary returned by to_dict method"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        self.assertIn('created_at', model_dictionary)

    def test_to_dict_created_at_str(self):
        """test type of 'created_at' value is a str"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        self.assertEqual(str, type(model_dictionary['created_at']))

    def test_dict_to_instance(self):
        """test dict -> instance"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        m2 = BaseModel(**model_dictionary)
        self.assertEqual(type(m), type(m2))

    def test_dict_to_id_attr(self):
        """test dict -> instance's id attr"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        m2 = BaseModel(**model_dictionary)
        self.assertEqual(m.id, m2.id)

    def test_dict_to_id_attr_type(self):
        """test dict -> instance's id attr"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        m2 = BaseModel(**model_dictionary)
        self.assertEqual(str, type(m2.id))

    def test_dict_to_updated_at_attr(self):
        """test dict -> instance's updated_at attr"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        m2 = BaseModel(**model_dictionary)
        self.assertEqual(m.updated_at, m2.updated_at)

    def test_dict_to_updated_at_attr_type(self):
        """test dict -> instance's updated_at attr type"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        m2 = BaseModel(**model_dictionary)
        self.assertEqual(type(datetime.now()), type(m2.updated_at))

    def test_dict_to_created_at_attr(self):
        """test dict -> instance's created_at attr"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        m2 = BaseModel(**model_dictionary)
        self.assertEqual(m.created_at, m2.created_at)

    def test_dict_to_created_at_attr_type(self):
        """test dict -> instance's created_at attr type"""
        m = BaseModel()
        model_dictionary = m.to_dict()
        m2 = BaseModel(**model_dictionary)
        self.assertEqual(type(datetime.now()), type(m2.created_at))
