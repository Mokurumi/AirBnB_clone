#!/usr/bin/python3
"""
This module describes tests for the file storage model class
"""


import unittest
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    This class tests functionality of FileStorage class
    """

    def setUp(self):
        """Set up a clean environment for testing."""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.test_data = {
            "id": "test_id",
            "created_at": "2023-10-15T12:30:45.123456",
            "updated_at": "2023-10-15T12:45:30.654321",
            "name": "Test Model"
        }

    def tearDown(self):
        """Clean up any files generated during testing."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test the all method of FileStorage."""
        data = self.storage.all()
        self.assertIsInstance(data, dict)

    def test_new(self):
        """Test the new method of FileStorage."""
        self.storage.new(self.base_model)
        key = "{}.{}".format(
                self.base_model.__class__.__name__, self.base_model.id
                )
        data = self.storage.all()
        self.assertIn(key, data)

    def test_save(self):
        """Test the save method of FileStorage."""
        key = "{}.{}".format(
                self.base_model.__class__.__name__, self.base_model.id
                )
        self.storage.new(self.base_model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    # def test_reload(self):
        # """Test the reload method of FileStorage."""
        # self.storage.new(self.base_model)
        # self.storage.save()
        # self.storage.reload()
        # data = self.storage.all()
        # key = "{}.{}".format(
        #         self.base_model.__class__.__name__, self.base_model.id
        #         )
        # self.assertIn(key, data)


if __name__ == "__main__":
    unittest.main()
