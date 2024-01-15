#!/usr/bin/python3
"""
tests/test_engine/test_file_storage
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create a unique FileStorage instance for testing
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        # Remove the test JSON file if it exists
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_save_and_reload(self):
        # Test saving and reloading objects
        model1 = BaseModel()
        model2 = BaseModel()

        # Save the objects
        self.storage.new(model1)
        self.storage.new(model2)
        self.storage.save()

        # Check if the JSON file is created
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

        # Reload the objects
        self.storage.reload()

        # Check if the objects are correctly stored in __objects
        self.assertIn(f"BaseModel.{model1.id}", self.storage.all())
        self.assertIn(f"BaseModel.{model2.id}", self.storage.all())

    def test_add_new_objects(self):
        # Test adding new objects to __objects
        model1 = BaseModel()
        model2 = BaseModel()

        # Add the objects
        self.storage.new(model1)
        self.storage.new(model2)

        # Check if the objects are correctly stored in __objects
        self.assertIn(f"BaseModel.{model1.id}", self.storage.all())
        self.assertIn(f"BaseModel.{model2.id}", self.storage.all())

    def test_retrieve_all_objects(self):
        # Test retrieving all objects from __objects
        model1 = BaseModel()
        model2 = BaseModel()

        # Save the objects
        self.storage.new(model1)
        self.storage.new(model2)
        self.storage.save()

        # Retrieve all objects
        all_objects = self.storage.all()

        # Check if the returned dictionary contains the expected objects
        self.assertIn(f"BaseModel.{model1.id}", all_objects)
        self.assertIn(f"BaseModel.{model2.id}", all_objects)

if __name__ == '__main__':
    unittest.main()
