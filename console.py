# #!/usr/bin/python3
# """The HBnB console."""

import cmd
from models import storage
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter."""

    prompt = "(hbnb) "
   t__models = {
        "BaseModel", "User", "State", "City", "Place", "Amenity", "Review"
    }

    def do_quit(self, args):
        """Exit The Program."""
        return True

    def do_EOF(self, args):
        """Exit The Program useing End-of-File(Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.t__models:
            print("** class doesn't exist **")
            return

        ob_j = eval(args[0])()  # creates an instance
        ob_j.save()
        print(ob_j.id)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.t__models:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[f"{args[0]}.{args[1]}"])

