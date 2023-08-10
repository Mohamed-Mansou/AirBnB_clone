#!/usr/bin/python3
"""  class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """

class FileStorage:
    
    __file_path = "file.json"
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
        """ serializes __objects to the JSON file """
        pass
    def reload(self):
        """ deserializes the JSON file to __objects """
        pass