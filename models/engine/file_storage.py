#!/usr/bin/python3
"""file storage for creating writing and reading json for storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class for storage

    attributes:
        _file_path (str):
        __objects (dict):
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        file_id = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[file_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fileName = self.__file_path
        fileObj = self.__objects
        storeD = {obj: fileObj[obj].to_dict() for obj in fileObj.keys()}
        with open(fileName, "w") as fN:
            json.dump(storeD, fN)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file exists;
        otherwise, do nothing. If the file doesn’t exist, no exception  raised)
        """
        fileName = self.__file_path
        FileStorage.__objects = {}
        try:
            with open(fileName) as StrJ:
                storeD = json.load(StrJ)
        except FileNotFoundError:
            return
        for value in storeD.values():
            clsName = value["__class__"]
            del value["__class__"]
            self.new(eval(clsName)(**value))
