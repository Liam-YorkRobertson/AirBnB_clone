#!/usr/bin/python3
"""
Command interpreter for the HBNB project
"""
import cmd
import json
import models


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
        Create new instance of BaseModel.
        """
        if not arg:
            print("** class name missing **")
            return ()

        try:
            new_inst = models.classes[arg]()
            new_inst.save()
            print(new_inst.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show string representation of instance.
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
        Prints all instances based or not on the class name.
        """
        objects = models.storage.all()

        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in models.classes:
                print("** class doesn't exist **")
                return ()

            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == args[0]])

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

        attribute_name = args[2]
        attribute_value = args[3]

        if hasattr(inst, attribute_name):
            setattr(inst, attribute_name,
                    type(getattr(inst, attribute_name))(attribute_value))
            inst.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
