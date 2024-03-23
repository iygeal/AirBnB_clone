#!/usr/bin/python3
"""Test module for the Amenity class"""

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """This class tests the Amenity class"""

    def test_public_attributes(self):
        """Tests for the public class attributes"""

        # Instantiate class
        my_instance = Amenity()

        # Assert that the Amenity instance has the public attribute
        self.assertTrue(hasattr(my_instance, "name"))

        # Assert that the public instance is an empty string
        assert (my_instance.name == "")


if __name__ == "__main__":
    unittest.main()
