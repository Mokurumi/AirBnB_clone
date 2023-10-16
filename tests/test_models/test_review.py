#!/usr/bin/python3
"""
This module describes tests for the user model class
"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''
    this class tests functionality of Review class
    '''
    def test_review_attributes(self):
        """
        Test if Review class attributes are correctly initialized.
        """
        review = Review()

        # Check if review attributes are correctly initialized
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_inheritance(self):
        """
        Test if Review class properly inherits from BaseModel.
        """
        review = Review()

        # Check if Review class inherits from BaseModel
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(review, Review)


if __name__ == '__main__':
    unittest.main()
