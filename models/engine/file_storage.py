#!/usr/bin/python3
"""  class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
import json
import os
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State

class FileStorage:
    
    __file_path = 'file.json'
    __objects={}
    
    """ Public instance methods"""
    
    def all(self):
        """ returns the dictionary of__objects """
        return self.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""

        obj_id = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[obj_id] = obj
        
    def save(self):
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    
    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                new_obj_dict = json.load(f)
            for value in new_obj_dict.values():
                class_Name = value["__class__"]
                self.new(eval(class_Name)(**value))
        except FileNotFoundError:
            pass
