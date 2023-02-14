"""Testing the `base_model` module."""
import unittest
import uuid
from datetime import datetime, timedelta
from models import storage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """ Set up method to run before each test case """
        self.base_model = BaseModel()

    def test_instantiation(self):
        """ Test instantiation of BaseModel """
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id(self):
        """ Test the id is a string """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """ Test creation time is set properly """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """ Test update time is set properly """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """ Test the save method updates the updated_at attribute """
        prev_update_time = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, prev_update_time)

    def test_to_dict(self):
        """ Test the to_dict method returns a dictionary """
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
