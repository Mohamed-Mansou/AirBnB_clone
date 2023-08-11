#!/usr/bin/python3

""" Base model class which is the parent class"""

import models
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """ re-create an instance with this dictionary representation."""
        now = datetime.now()
        self.id = str(uuid.uuid4()) if "id" not in kwargs else kwargs.get("id")
        self.created_at = now if "created_at" not in kwargs else kwargs.get("created_at")
        self.updated_at = now if "updated_at" not in kwargs else kwargs.get("updated_at")
        for key, value in kwargs.items():
            if key == "created_at" or key == "updated_at":
                setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            else:
                setattr(self, key, value)
        models.storage.new(self)
    def __str__(self):
        """ the string representation"""
        return "[{}],({}),{}".format(self.__class__.__name__,self.id,self.__dict__)
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        """ import storage variable"""
        models.storage.save()
        
    def to_dict(self):
        """  returns a dictionary containing all keys/values of __dict__ of the instance """
        this_my_dict = self.__dict__.copy()
        this_my_dict["created_at"] = self.created_at.isoformat()
        this_my_dict["updated_at"] = self.updated_at.isoformat()
        this_my_dict["__class__"] = self.__class__.__name__
        return this_my_dict