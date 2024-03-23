#!/usr/bin/python3
"""Test module for the User class"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """This class tests the User class"""

    def test_public_attributes(self):
        """Tests for the public class attributes"""

        # Instance of User
        my_user = User()

        # Assert that the User instance has the public attributes
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))

        # Assert that the public instances are empty strings
        assert (my_user.email == "")
        assert (my_user.password == "")
        assert (my_user.first_name == "")
        assert (my_user.last_name == "")


if __name__ == "__main__":
    unittest.main()
