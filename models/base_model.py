#!/usr/bin/python3
"""This script is the base model"""

import models
import uuid
from datetime import datetime



class BaseModel:
    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """ instantiates an object with its attributes """
        if kwargs:
                for key, value in kwargs.items():
                    if key != "__class__":
                        setattr(self, key, value)
                if "created_at" in kwargs:
                    self.created_at = datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
                if "updated_at" in kwargs:
                    self.updated_at = datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
                return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        my_dict = {**self.__dict__}
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at
        my_dict['updated_at'] = self.updated_at
        return my_dict
