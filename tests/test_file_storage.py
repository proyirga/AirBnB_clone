"""Testing the `FileStorage` module."""
import unittest
import os
import json
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test.json'
        storage._FileStorage__file_path = self.file_path
        storage.__objects = {}

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        bm = BaseModel()
        bm.name = 'Noah'
        bm.age = 25
        bm.save()

        objects = storage.all()
        expected = {'BaseModel.{}'.format(bm.id): bm.to_dict()}
        self.assertEqual(objects, expected)

    def test_new(self):
        bm = BaseModel()
        bm.name = 'Noah'
        bm.age = 25
        storage.new(bm)

        objects = storage.all()
        expected = {'BaseModel.{}'.format(bm.id): bm.to_dict()}
        self.assertEqual(objects, expected)

    def test_save(self):
        bm = BaseModel()
        bm.name = 'Noah'
        bm.age = 25
        bm.save()

        with open(self.file_path, 'r') as f:
            data = json.load(f)
            expected = {'BaseModel.{}'.format(bm.id): bm.to_dict()}
            self.assertEqual(data, expected)

    def test_reload(self):
        bm = BaseModel()
        bm.name = 'Noah'
        bm.age = 25
        bm.save()

        storage.__objects = {}
        storage.reload()

        objects = storage.all()
        expected = {'BaseModel.{}'.format(bm.id): bm.to_dict()}
        self.assertEqual(objects, expected)
