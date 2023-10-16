#!/usr/bin/python3
"""
This module describes tests for the user model class
"""


import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        """
        Test if User class attributes are correctly initialized.
        """
        user = User()

        # Check if user attributes are correctly initialized
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inheritance(self):
        """
        Test if User class properly inherits from BaseModel.
        """
        user = User()

        # Check if User class inherits from BaseModel
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
