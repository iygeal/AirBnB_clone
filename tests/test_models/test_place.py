#!/usr/bin/python3
"""Test Module for the Place class"""

from models.place import Place
import unittest


class TestPlaceClass(unittest.TestCase):
    """Class to test for Place"""

    def test_place(self):
        """Test method for the Place class"""
        # Instantiate Place
        my_place = Place()

        # Test for public class attributes
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertTrue(hasattr(my_place, "name"))
        self.assertTrue(hasattr(my_place, "description"))
        self.assertTrue(hasattr(my_place, "number_rooms"))
        self.assertTrue(hasattr(my_place, "number_bathrooms"))
        self.assertTrue(hasattr(my_place, "max_guest"))
        self.assertTrue(hasattr(my_place, "price_by_night"))
        self.assertTrue(hasattr(my_place, "latitude"))
        self.assertTrue(hasattr(my_place, "longitude"))
        self.assertTrue(hasattr(my_place, "amenity_ids"))

        # Check for their assigned values
        assert (my_place.city_id == "")
        assert (my_place.user_id == "")
        assert (my_place.name == "")
        assert (my_place.description == "")
        assert (my_place.number_bathrooms == 0)
        assert (my_place.number_rooms == 0)
        assert (my_place.max_guest == 0)
        assert (my_place.price_by_night == 0)
        assert (my_place.latitude == 0.0)
        assert (my_place.longitude == 0.0)
        assert (my_place.amenity_ids == [])


if __name__ == "__main__":
    unittest.main()
