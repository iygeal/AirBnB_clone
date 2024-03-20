#!/usr/bin/python3
"""Module to test FileStorage"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """Class to test FileStorage"""

    def setUp(self):
        """Instances for test methods"""
        self.obj_1 = FileStorage()
        self.obj_2 = FileStorage()
        self.base_1 = BaseModel()

    def tearDown(self):
        """ Remove file.json after testing"""
        try:
            os.remove("file.json")
        except Exception as e:
            pass

    def test_FileStorage_attributes(self):
        """Tests for present attributes"""
        self.assertTrue(hasattr(self.obj_1, '_FileStorage__objects'))
        self.assertTrue(hasattr(self.obj_1, '_FileStorage__file_path'))

    def test_save_method(self):
        """Tests for the save() method"""

        # Check that our file (file.json) is not in path before calling save()
        self.assertFalse(os.path.exists("file.json"))

        # Call save() on object to  trigger the serialization
        # and file writing processes
        self.obj_1.save()

        # Check that "file.json" now exists
        self.assertTrue(os.path.exists("file.json"))

    def test_new_method(self):
        """Tests the behaviour of the new() method"""
        new_obj = self.base_1
        self.obj_1.new(new_obj)

        # Check that new_obj class name and id are in __objects as key
        self.assertIn(f"{new_obj.__class__.__name__}.{new_obj.id}",
                      FileStorage._FileStorage__objects.keys())

        # Check that 'new_obj' is a value in __objects
        self.assertIn(new_obj, FileStorage._FileStorage__objects.values())
