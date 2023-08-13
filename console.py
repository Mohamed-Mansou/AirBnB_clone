#!/usr/bin/env python3
"""The HBnB console that contains
the entry point of the command interpreter"""


import cmd
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter."""

    prompt = "(hbnb) "
    __mod_els = {
        "BaseModel", "User", "State", "City", "Place", "Amenity", "Review"
    }

    def do_quit(self, args):
        """Exit The Program."""
        return True

    def do_EOF(self, args):
        """Exit The Program using End-of-File(Eof) with (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.__mod_els:
            print("** class doesn't exist **")
            return

        inst = eval(args[0])()
        inst.save()
        print(inst.id)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.__mod_els:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id."""
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.__mod_els:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        del storage.all()["{}.{}".format(args[0], args[1])]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances"""
        obj_s = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in obj_s.values()])
            return
        args = args.split()
        if args[0] not in self.__mod_els:
            print("** class doesn't exist **")
            return
        t_all = []
        for obj in obj_s.values():
            if obj.__class__.__name__ == args[0]:
                all.append(str(obj))
        print(t_all)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        obj_s = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.__mod_els:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in obj_s:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        if args[3].isdigit():
            a_val = int(args[3])
        else:
            try:
                a_val = float(args[3])
            except ValueError:
                a_val = args[3].replace('"', "")
        for key, obj in obj_s.items():
            if["{}.{}".format(args[0], args[1])] == key: 
                setattr(obj, args[2], a_val)
                storage.save()
                return

    def default(self, line):
        """
        handle dot notaion commands
        """
        if '.' in line:
            cls, methd, *args = line.split('.')

        if methd == 'all':
            print('[', end='')
            for obj in storage.all().values():
                if obj.__class__.__name__ == cls:
                    print(obj, end='')
            print(']')

        elif methd == 'count':
            all = []
            for obj in storage.all().values():
                if obj.__class__.__name__ == cls:
                    all.append(obj)
            print(len(all))

        elif methd.startswith('show'):
            id = args[0]
            self.do_show(f'{cls}.{id}'.format(cls, id))

        elif methd.startswith('destroy'):
            id = args[0]
            self.do_destroy(f'{cls} {id}')

        elif methd.startswith('update'):
            id = args[0]
            attr = args[1]
            if ',' in attr:
                try:
                    attr = json.loads(attr.replace("'", '"'))
                    for k, v in attr.items():
                        print(f'{cls} {id} {k} {v}')
                        self.do_update(f'{cls} {id} {k} {v}')
                except Exception as e:
                    print(f'Error: {e}')
            else:
                attr = attr.split('"')[1]
                self.do_update(f'{cls} {id} {attr} {args[2]}')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
