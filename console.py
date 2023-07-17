#!/usr/bin/python3
"""
Command interpreter for the HBNB project
"""
import cmd
import json
import models
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models import *
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Sets Commands for the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return (True)

    def do_EOF(self, arg):
        """
        Exits program with EOF.
        """
        return (True)

    def emptyline(self):
        """
        Do nothing if empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel.
        """
        if not arg:
            print("** class name missing **")
            return ()

        try:
            new_inst = eval(arg)()
            new_inst.save()
            print(new_inst.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        """
        if not arg:
            print("** class name missing **")
            return ()

        args = arg.split()
        class_name = args[0]
        objects = storage.all()

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return ()

        if len(args) < 2:
            print("** instance id missing **")
            return ()

        inst_key = class_name + '.' + args[1]
        inst = objects.get(inst_key, None)
        if inst:
            print(inst)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy an instance.
        """
        if not arg:
            print("** class name missing **")
            return ()

        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return ()

        if len(args) < 2:
            print("** instance id missing **")
            return ()

        objects = models.storage.all()
        inst_key = args[0] + '.' + args[1]
        inst = objects.get(inst_key, None)
        if inst:
            del objects[inst_key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string representation of all instances.
        """
        objects = storage.all()

        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
                return ()

            print([str(obj) for obj in objects.values()
                  if type(obj).__name__ == class_name])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return ()

        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return ()

        if len(args) < 2:
            print("** instance id missing **")
            return ()

        objects = models.storage.all()
        inst_key = args[0] + '.' + args[1]
        inst = objects.get(inst_key, None)
        if not inst:
            print("** no instance found **")
            return ()

        if len(args) < 3:
            print("** attribute name missing **")
            return ()

        if len(args) < 4:
            print("** value missing **")
            return ()

        attr_name = args[2]
        attr_value = args[3]

        if attr_name == "id" or attr_name == "created_at" \
                or attr_name == "updated_at":
            return ()

        setattr(inst, attr_name, attr_value)
        inst.save()

    def default(self, line):
        """
        Allows use of <class name>.all().
        """
        match = re.match(r'^(\w+)\.all\(\)$', line)
        if match:
            class_name = match.group(1)
            if class_name in models.classes:
                objects = storage.all()
                print([str(obj) for obj in objects.values()
                       if type(obj).__name__ == class_name])
            else:
                print("** class doesn't exist **")
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
