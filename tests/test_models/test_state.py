#!/usr/bin/python3
"""
This module describes tests for the state model class
"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''
    this class test the functionality of State class
    '''
    def test_state_attributes(self):
        """
        Test if State class attributes are correctly initialized.
        """
        state = State()

        # Check if state attributes are correctly initialized
        self.assertEqual(state.name, "")

    def test_state_inheritance(self):
        """
        Test if State class properly inherits from BaseModel.
        """
        state = State()

        # Check if State class inherits from BaseModel
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(state, State)


if __name__ == '__main__':
    unittest.main()
