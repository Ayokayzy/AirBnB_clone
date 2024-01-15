#!/usr/bin/python3
"""
tests/test_models/test_city.py
"""


import unittest
import os
from models.city import City
from models.engine.file_storage import FileStorage

class TestUserModel(unittest.TestCase):

    def setUp(self):
        # Create a unique FileStorage instance for testing
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        # Remove the test JSON file if it exists
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create_and_save_city(self):
        # Test creating and saving City objects
        city1 = City()
        city2 = City()

        # Save the objects
        self.storage.save()

        # Check if the JSON file is created
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_user_objects(self):
        # Test reloading User objects
        city1 = City()
        city2 = City()
       

        # Save the objects
        self.storage.save()

        # Reload the objects
        self.storage.reload()

        # Check if the objects are correctly stored in __objects
        self.assertIn(f"City.{city1.id}", self.storage.all())
        self.assertIn(f"City.{city2.id}", self.storage.all())

if __name__ == '__main__':
    unittest.main()
