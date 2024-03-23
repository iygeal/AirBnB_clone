#!/usr/bin/python3
"""Module to test the Review class using unittest"""

from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Test class for Review"""

    def test_public_class_attributes(self):
        """Test method for the Review class"""

        # Instantiate a Review object
        reviews = Review()

        # Test for public class attributes
        self.assertTrue(hasattr(reviews, "place_id"))
        self.assertTrue(hasattr(reviews, "user_id"))
        self.assertTrue(hasattr(reviews, "text"))

        # Check that they are empty strings
        assert (reviews.place_id == "")
        assert (reviews.user_id == "")
        assert (reviews.text == "")


if __name__ == "__main__":
    unittest.main()
