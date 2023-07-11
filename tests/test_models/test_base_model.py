#!/usr/bin/python3
"""
Unit tests for BaseModel.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_id_is_string(self):
        """
        Test if id attribute is a string.
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test if created_at attribute is a datetime object.
        """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if updated_at attribute is a datetime object.
        """
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """
        Test __str__ method.
        """
        model = BaseModel()
        model_str = str(model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(model.id, model_str)

    def test_save_updates_updated_at(self):
        """
        Test if save method updates the updated_at attribute.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_returns_dictionary(self):
        """
        Test if to_dict method returns a dictionary.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_has_correct_keys(self):
        """
        Test if to_dict method returns a dictionary with the correct keys.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)


if __name__ == '__main__':
    unittest.main()
