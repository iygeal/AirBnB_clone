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

    def test_custom_attributes(self):
        """Tests BaseModel with custom attributes"""
        self.base_1.number = 38000000000
        self.base_1.money = "Thirty Eight Billion Dollars"
        self.assertCountEqual(
            self.base_1.money, 'Thirty Eight Billion Dollars')
        self.assertEqual(self.base_1.number, 38000000000)

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
        view = f"[BaseModel] ({self.base_1.id}) {self.base_1.__dict__}"
        self.assertEqual(view, str(self.base_1))

    def test_save_method(self):
        """Tests if save() updates updated_at"""
        base_3 = BaseModel()
        base_3.save()
        self.assertNotEqual(self.base_1.updated_at, base_3.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method is as expected"""

        # Check if all existing keys are passed accordingly
        dict_instance = self.base_1.__dict__
        for key in dict_instance:
            self.assertIn(key, self.base_1.to_dict())

        # Check if __class__ is added and assigned accordingly
        new_dict = self.base_1.to_dict()
        self.assertEqual(new_dict['__class__'], self.base_1.__class__.__name__)

        # Check if datetime objects were converted to strings
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)

    def test_keyworded_args_not_empty(self):
        """Tests for when **kwargs is not empty"""
        test_dict = self.base_1.to_dict()
        base_4 = BaseModel(**test_dict)
        self.assertEqual(test_dict, base_4.to_dict())

    def test_empty_keyworded_args(self):
        """Tests if an empty dict is passed to kwargs"""
        empty_dict = {}
        base_5 = BaseModel(**empty_dict)
        self.assertIn('id', base_5.__dict__)
        self.assertIn('created_at', base_5.__dict__)
        self.assertIn('updated_at', base_5.__dict__)


if __name__ == "__main__":
    unittest.main()
