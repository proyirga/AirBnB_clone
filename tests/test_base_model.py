"""Testing the `base_model` module."""
import json
import os
import time
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def setUp(self):
        """Set up method that runs before each test"""
        self.model = BaseModel()

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual(type(self.model.to_dict()), dict)
        self.assertTrue(hasattr(self.model.to_dict(), "__class__"))

    def test_str(self):
        """Test str method"""
        self.assertEqual(str(self.model),
                         "[BaseModel] ({}) {}".format(
                             self.model.id, self.model.__dict__
                         ))


if __name__ == '__main__':
    unittest.main()
