#!/usr/bin/python3
"""Test module for State class"""

from models.state import State
import unittest


class TestState(unittest.TestCase):
    """This class tests the State class"""

    def test_public_attributes(self):
        """Tests for the public class attributes"""

        # Instance of State
        my_instance = State()

        # Assert that the State instance has the public attribute
        self.assertTrue(hasattr(my_instance, "name"))

        # Assert that the public instance is an empty string
        assert (my_instance.name == "")


if __name__ == "__main__":
    unittest.main()
