#!/usr/bin/python3

""" Base model class which is the parent class"""

import models
from datetime import datetime
import uuid


class BaseModel:
    """Represents the BaseModel of Task"""
    def __init__(self, *args, **kwargs):
        """intial a BaseModel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """updates attribute updated_at with the current datetime """
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Print: [<class name>] (<self.id>) <self.__dict__> """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
