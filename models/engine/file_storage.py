#!/usr/bin/python3

""" Module: file_storage.py """

import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        dic = {}
        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            f.write(json.dumps(dic))

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """

        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                dic = json.loads(f.read())
                for key, value in dic.items():
                    class_name = value["__class__"]
                    if class_name == "User":
                        FileStorage.__objects[key] = User(**value)
                    else:
                        FileStorage.__objects[key] = eval("{}(**value)".format(class_name))
        except FileNotFoundError:
            pass
