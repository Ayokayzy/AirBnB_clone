#!/usr/bin/python
"""
models/engine/file_storage.py
"""
import json
import os.path
from models.base_model import BaseModel

all_class = {
    "BaseModel": BaseModel
}

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        my_dict = {key: value.to_dict() for key,
                   value in self.__objects.items()}
        with open(self.__file_path, "w") as fp:
            json.dump(my_dict, fp)

    def reload(self):
        """
        deserializes the JSON file to __objects
        if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        #load string from file to a string
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as fp:
            self.__objects = {
                    key: all_class[val["__class__"]](**val)
                    for key, val in json.load(fp).items()
                }