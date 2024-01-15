#!/usr/bin/python3
# """Defines unittests for base_model.py.

# Unittest classes:
#     TestBaseModelInstantiation
# """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_instantiation(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsNotNone(b1.id)
        self.assertIsNotNone(b1.created_at)
        self.assertIsNotNone(b1.updated_at)
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_str_method(self):
        # Test __str__ method
        model = BaseModel()
        str_representation = str(model)
        self.assertIn(f"[{model.__class__.__name__}]", str_representation)
        self.assertIn(f"({model.id})", str_representation)

    def test_save_method(self):
        # Test save method
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict_method(self):
        # Test to_dict method
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], model.__class__.__name__)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_to_dict_method(self):
        # Test to_dict method
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], model.__class__.__name__)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_init_from_dict(self):
        # Test __init__ method with dictionary representation
        model = BaseModel()
        model_dict = model.to_dict()

        # Modify the created_at and updated_at values to be strings
        model_dict["created_at"] = model.created_at.isoformat()
        model_dict["updated_at"] = model.updated_at.isoformat()

        # Recreate an instance from the dictionary
        recreated_model = BaseModel(**model_dict)

        # Check if the recreated model has the same attributes
        self.assertEqual(recreated_model.id, model.id)
        self.assertEqual(recreated_model.created_at, model.created_at)
        self.assertEqual(recreated_model.updated_at, model.updated_at)

if __name__ == '__main__':
    unittest.main()
