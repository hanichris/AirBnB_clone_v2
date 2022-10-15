#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of all the models currently in storage.

        If a particular class is required, return only the objects
        belonging to that class. The class serves as an optional filter.

        Args:
            cls (class): Class to filter the dictonary of objects by.
        """
        if cls is not None:
            return {
                    key: value
                    for key, value in FileStorage.__objects.items()
                    if key.startswith(f'{cls.__name__}')
                    }
        return FileStorage.__objects

    def new(self, obj):
        """ Insert `obj` into the class attribute `__objects`.

        The key used in the dictionary `__objects` is the id of
        the object. The format is `<class name>.id` eg BaseModel.123

        Args:
            obj (object): instance of a class.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """ Deletes an object from the class attribute `__objects`.

        Args:
            obj (BaseModel): object to be removed from `__objects`.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if FileStorage.__objects.get(key):
                del FileStorage.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
