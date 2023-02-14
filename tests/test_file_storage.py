#Testing the `FileStorage` module.
import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    
    def setUp(self):
        self.storage = FileStorage()
    
    def test_all_returns_dictionary(self):
        self.assertIsInstance(self.storage.all(), dict)
    
    def test_new_adds_object_to_dictionary(self):
        class TestObj:
            id = "test_id"
        
        obj = TestObj()
        self.storage.new(obj)
        self.assertIn("TestObj.test_id", self.storage.all())
    
    def test_save_writes_to_file(self):
        class TestObj:
            id = "test_id"
            def to_dict(self):
                return {"id": self.id}
        
        obj = TestObj()
        self.storage.new(obj)
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, "r") as f:
            contents = f.read()
            self.assertIn("test_id", contents)
    
    def test_classes_returns_dict(self):
        self.assertIsInstance(self.storage.classes(), dict)
    
    def test_reload_loads_file(self):
        class TestObj:
            id = "test_id"
            def to_dict(self):
                return {"id": self.id}
        
        obj = TestObj()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn("TestObj.test_id", self.storage.all())
    
    def test_attributes_returns_dict(self):
        self.assertIsInstance(self.storage.attributes(), dict)

        
if __name__ == "__main__":
    unittest.main()
