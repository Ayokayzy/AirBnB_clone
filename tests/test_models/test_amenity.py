#!/usr/bin/python3
"""
tests/test_models/test_amenity.py
"""


import unittest
import os
from models.amenity import Amenity
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

    def test_create_and_save_amenity(self):
        # Test creating and saving City objects
        amenity1 = Amenity()
        amenity2 = Amenity()

        # Save the objects
        self.storage.save()

        # Check if the JSON file is created
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_amenity_objects(self):
        # Test reloading Amenity objects
        amenity1 = Amenity()
        amenity2 = Amenity()
       

        # Save the objects
        self.storage.save()

        # Reload the objects
        self.storage.reload()

        # Check if the objects are correctly stored in __objects
        self.assertIn(f"Amenity.{amenity1.id}", self.storage.all())
        self.assertIn(f"Amenity.{amenity2.id}", self.storage.all())

if __name__ == '__main__':
    unittest.main()
