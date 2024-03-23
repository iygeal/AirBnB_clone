#!/usr/bin/python3
"""Test module for the City class"""

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """This class tests the City class"""

    def test_public_attributes(self):
        """Tests for the public class attributes"""

        # Instance of of the class
        my_instance = City()

        # Assert that the instance has the public attributes
        self.assertTrue(hasattr(my_instance, "state_id"))
        self.assertTrue(hasattr(my_instance, "name"))

        # Assert that the public instance is an empty string
        assert (my_instance.state_id == "")
        assert (my_instance.name == "")


if __name__ == "__main__":
    unittest.main()
