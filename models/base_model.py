#!/usr/bin/python3

""" Base model class which is the parent class"""

import models
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initialize the object.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Set attributes from kwargs.
        for key, value in kwargs.items():
            if key == "updated_at" or key == "created_at":
                setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            elif key != "__class__":
                setattr(self, key, value)

        # If id is not in kwargs, set it to a new uuid.
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()
        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()
        # Add the object to the storage.
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