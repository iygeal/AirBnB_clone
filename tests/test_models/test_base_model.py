#!/usr/bin/python3
"""Module for BaseModel test suite"""

from models.base_model import BaseModel
import os
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """The class to test BaseModel"""

    def setUp(self):
        """Creates instances to test BaseModel"""
        self.base_1 = BaseModel()
        self.base_2 = BaseModel()

    def test_BaseModel_instance(self):
        """Tests for BaseModel objects"""
        self.assertIsInstance(self.base_1, BaseModel)

    def test_BaseModel_attributes(self):
        """Tests for BaseModel attributes"""
        self.assertTrue(hasattr(self.base_1, "created_at"))
        self.assertTrue(hasattr(self.base_1, "updated_at"))
        self.assertTrue(hasattr(self.base_1, "id"))

    def test_attribute_types(self):
        """Tests the class types of BaseModel attributes"""
        self.assertIsInstance(self.base_1.id, str)
        self.assertIsInstance(self.base_1.created_at, datetime)
        self.assertIsInstance(self.base_1.updated_at, datetime)

    def test_unique_id(self):
        """Tests if IDs are unique"""
        self.assertNotEqual(self.base_1.id, self.base_2.id)

    def test_str_visualization(self):
        """Tests if __str__() correctly visualizes BaseModel"""
        expected_view = f"[BaseModel] ({self.base_1.id}) {self.base_1.__dict__}"
        self.assertEqual(expected_view, str(self.base_1))

    def test_save_method(self):
        """Tests if save() updates updated_at"""
        base_3 = BaseModel()
        base_3.save()
        self.assertNotEqual(self.base_1.updated_at, base_3.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method is as expected"""
        new_dict = self.base_1.to_dict()

        # Check if __class__ is added and assigned accordingly
        self.assertEqual(new_dict['__class__'], self.base_1.__class__.__name__)

        # Check if datetime objects were converted to strings
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
