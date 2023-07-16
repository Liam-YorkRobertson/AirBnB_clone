#!/usr/bin/python3
"""
file storage for creating writing and reading json for storage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    for file storage
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        returns the dictionary __objects
        """
        FileObj = FileStorage.__objects
        return Fileobj

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        file_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[file_id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        fileName = FileStorage.__file_path
        fileObj = FileStorage.__objects
        storeD = {obj: fileObj[obj].to_dict() for obj in fileObj.keys()}
        with open(fileName, "w") as fN:
            json.dump(storeD, fN)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file exists;
        otherwise, do nothing. If the file doesn’t exist, no exception  raised)
        """
        fileName = FileStorage.__file_path
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

    def delete(self, obj=None):
        """Deletes an object if it exists."""
        FileId = "{}.{}".format(type(obj).__name__, obj.id)
        FileObj = FileStorge._objects
        try:
            del FileObj[FileId]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the reload function"""
        FileStorage.reload()
