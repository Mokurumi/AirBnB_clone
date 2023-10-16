#!/usr/bin/python3
"""
This module describes tests for the place model class
"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''
    this class tests the Place class functionality
    '''
    def test_place_attributes(self):
        """
        Test if Place class attributes are correctly initialized.
        """
        place = Place()

        # Check if place attributes are correctly initialized
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_inheritance(self):
        """
        Test if Place class properly inherits from BaseModel.
        """
        place = Place()

        # Check if Place class inherits from BaseModel
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(place, Place)


if __name__ == '__main__':
    unittest.main()
