#!/usr/bin/python3
"""The HBnB console."""

import cmd
import json
import os
from models.city import City
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit The Program."""
        return True

    def do_EOF(self, arg):
        """Exit The Program using End-of-File """
        print('')
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""


        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 1:
            print("** instance id missing **")
            return
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
