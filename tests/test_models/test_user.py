#!/usr/bin/python3
"""
tests/test_models/test_user.py
"""


import unittest
import os
from models.user import User
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

    def test_create_and_save_user(self):
        # Test creating and saving User objects
        user1 = User()
        user1.email = "user1@example.com"
        user1.password = "password1"
        user1.first_name = "John"
        user1.last_name = "Doe"
        user2 = User()
        user2.email = "user2@example.com"
        user2.password = "password2"
        user2.first_name = "Jane"
        user2.last_name = "Doe"

        # Add the objects
        # self.storage.new(user1)
        # self.storage.new(user2)

        # Save the objects
        self.storage.save()

        # Check if the JSON file is created
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_user_objects(self):
        # Test reloading User objects
        user1 = User()
        user1.email = "user1@example.com"
        user1.password = "password1"
        user1.first_name = "John"
        user1.last_name = "Doe"
        user2 = User()
        user2.email = "user2@example.com"
        user2.password = "password2"
        user2.first_name = "Jane"
        user2.last_name = "Doe"

        # Save the objects
        # self.storage.new(user1)
        # self.storage.new(user2)
        self.storage.save()

        # Reload the objects
        self.storage.reload()

        # Check if the objects are correctly stored in __objects
        self.assertIn(f"User.{user1.id}", self.storage.all())
        self.assertIn(f"User.{user2.id}", self.storage.all())

if __name__ == '__main__':
    unittest.main()
