#!/usr/bin/python3
"""Module to test FileStorage"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """Class to test FileStorage"""

    def setUp(self):
        """Instances for test methods"""
        self.obj_1 = FileStorage()
        self.obj_2 = FileStorage()
        self.base_1 = BaseModel()

    def test_FileStorage_attributes(self):
        """Tests for present attributes"""
        self.assertTrue(hasattr(self.obj_1, '_FileStorage__objects'))
        self.assertTrue(hasattr(self.obj_1, '_FileStorage__file_path'))

    def test_save_method(self):
        """Tests for the save() method"""
        self.base_1.save()
        file_dict = self.obj_1
        for key in _file_dict__objects.keys():
            self.assertIsInstance(_file_dict__objects[key], self.base_1.__class__.__name__)