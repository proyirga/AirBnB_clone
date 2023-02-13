#!/usr/bin/env python3

#Testing the `FileStorage` module.
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """ test for class FileStorage """

    def setUp(self):
        """ creates an instance of FileStorage """
        self.storage = FileStorage()
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_all(self):
        """ tests if all returns the FileStorage.__objects attribute """
        self.assertEqual(self.storage.all(), FileStorage.__objects)

    def test_new(self):
        """ tests if new adds an object to FileStorage.__objects """
        self.storage.new(self.user)
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        self.assertIn(key, FileStorage.__objects)

    def test_save(self):
        """ tests if save serializes __objects to the JSON file """
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage.__file_path))
        with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
            self.assertEqual(json.loads(f.read()), FileStorage.__objects)

    def test_reload(self):
        """ tests if reload deserializes the JSON file to __objects """
        self.storage.save()
        self.storage.reload()
        with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
            self.assertEqual(json.loads(f.read()), FileStorage.__objects)

if __name__ == "__main__":
    unittest.main()
