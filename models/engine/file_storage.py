#!/usr/bin/python3
"""  class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
import json
import os
import sys

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
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, 'w') as f:
            json.dump([obj.to_dict() for obj in self.__objects.values()], f)

    
    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                new_obj_dict = json.load(f)
            for value in new_obj_dict.values():
                class_name = value["__class__"]
                obj = getattr(sys.modules[class_name], "__new__")(**value)
                self.new(obj)
