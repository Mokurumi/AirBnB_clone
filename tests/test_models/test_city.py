#!/usr/bin/python3
"""
This module describes tests for the city model class
"""


import unittest
from models.user import User


class TestCity(unittest.TestCase):
    '''
    this class tests the City class
    '''
    def test_city_attributes(self):
        """
        Test if City class attributes are correctly initialized.
        """
        city = City()

        # Check if city attributes are correctly initialized
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_inheritance(self):
        """
        Test if City class properly inherits from BaseModel.
        """
        city = City()

        # Check if City class inherits from BaseModel
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(city, City)


if __name__ == '__main__':
    unittest.main()
