#!/usr/bin/python3
"""The HBnB console."""

import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit The Program."""
        return True

    def do_EOF(self, arg):
        """Exit The Program useing End-of-File(Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
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

        new_instance = eval(class_name)()
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
        elif len(args) == 1:
            print("** instance id missing **")
            return
        instance_key = f"{args[0]}.{args[1]}"
        all_instances = storage.all()
        if instance_key not in all_instances:
            print("** no instance found **")
            return
        else:
            all_instances.pop(instance_key)
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all"""
        obj_s = storage.all()
        if not args:
            print([str(obj) for obj in obj_s.values()])
            return
        args = args.split()
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        every = []
        for obj in obj_s.values():
            if obj.__class__.__name__ == args[0]:
                every.append(str(obj))
        print(every)

    def do_update(self, args):
        """ Updates an instance based on the class name and id"""
        obj_s = storage.all()
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if f"{args[0]}.{args[1]}" not in obj_s:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        if args[3].isdigit():
            t_value = int(args[3])
        else:
            try:
                t_value = float(args[3])
            except ValueError:
                t_value = args[3].replace('"', "")
        for key, obj in obj_s.items():
            if f"{args[0]}.{args[1]}" == key:
                setattr(obj, args[2], t_value)
                storage.save()
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
