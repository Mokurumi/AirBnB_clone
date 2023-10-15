#!/usr/bin/python3
"""
This module describes tests for the base model class
"""


import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """
    This class is used to test functionality of the BaseModel class
    """

    def setUp(self):
        """Set up a new BaseModel instance and test data."""
        self.base_model = BaseModel()
        self.test_data = {
            "id": "test_id",
            "created_at": "2023-10-15T12:30:45.123456",
            "updated_at": "2023-10-15T12:45:30.654321",
            "name": "Test Model"
        }
        self.base_model_from_dict = BaseModel(**self.test_data)

    def tearDown(self):
        """Clean up any files generated during testing."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_class_type(self):
        """Test if BaseModel is a class"""
        self.assertEqual(str(type(self.base_model)),
                "<class 'models.base_model.BaseModel'>")

    def test_id_property(self):
        """Test the id property of a BaseModel instance."""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """Test the created_at property of a BaseModel instance."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Test the updated_at property of a BaseModel instance."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_unique_ids(self):
        """Test the uniqueness of IDs for BaseModel instances."""
        num_instances = 100  # Number of instances to create for the test
        ids = set()  # A set to store generated IDs

        for _ in range(num_instances):
            new_instance = BaseModel()
            ids.add(new_instance.id)
        self.assertEqual(len(ids), num_instances)  # All IDs should be unique

    def test_new_instance(self):
        """Test creating a new BaseModel instance."""
        new_instance = BaseModel()
        self.assertIsInstance(new_instance, BaseModel)
        self.assertIsInstance(new_instance.id, str)

    def test_reload(self):
        """Test the reload method of BaseModel and storage."""
        # Save the BaseModel to a file
        storage.save()
        # Create a new BaseModel instance
        new_instance = BaseModel()
        # The new instance should not exist in memory, so reload it
        storage.reload()
        # The reloaded instance should have the same id as the new instance
        self.assertEqual(
                new_instance.id,
                storage.all()["BaseModel." + new_instance.id].id
                )

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        data = self.base_model.to_dict()
        self.assertEqual(type(data), dict)
        self.assertIn("__class__", data)
        self.assertEqual(data["__class__"], "BaseModel")
        self.assertIn("id", data)
        self.assertEqual(type(data["id"]), str)
        self.assertIn("created_at", data)
        self.assertIn("updated_at", data)
        self.assertIn("name", data)

    def test_from_dict(self):
        """Test the creation of a BaseModel instance from a dictionary."""
        data = self.test_data
        self.assertEqual(self.base_model_from_dict.id, data["id"])
        self.assertEqual(
                self.base_model_from_dict.created_at.isoformat(),
                data["created_at"]
                )
        self.assertEqual(
                self.base_model_from_dict.updated_at.isoformat(),
                data["updated_at"]
                )
        self.assertEqual(self.base_model_from_dict.name, data["name"])

    def test_save(self):
        """Test the save method of BaseModel."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_str(self):
        """Test the string representation of a BaseModel instance."""
        expected_str = "[BaseModel] ({}) {}".format(
                self.base_model.id, self.base_model.__dict__
                )
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == "__main__":
    unittest.main()
