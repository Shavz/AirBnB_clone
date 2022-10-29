#!/usr/bin/python3

"""
Contains the entry point of the command interpreter
"""

import cmd
from shlex import split
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage, cls_dict


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand inherits from cmd.Cmd
    """
    prompt = '(hbnb) '
    vc = cls_dict

    def do_create(self, arg):
        """
        Create command to create a new instance of BaseModel
        """
        if not arg:
            print('** class name missing **')
            return

        args = arg.split(" ")
        if args[0] in self.vc:
            new_model = eval("{}()".format(args[0]))
            new_model.save()
            print("{}".format(new_model.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show command to print string representation of instance
        based on the class name and id
        """
        obj = self.find_obj(arg)
        if obj:
            print(obj)

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance based on a class name and id
        and save changes to a JSON file
        """
        obj = self.find_obj(arg)
        if obj:
            objs = storage.all()
            del objs["{}.{}".format(type(obj).__name__, obj.id)]
            storage.save()

    def do_all(self, arg):
        """
        All command to print all instances based on a class name or
        all classes if none specified
        """
        objs = storage.all()
        ins = []
        if not arg:
            for o in objs:
                ins.append(objs[o])
            print(ins)
            return
        args = arg.split(" ")
        if args[0] in self.vc:
            for o in objs:
                if o[0:len(args[0])] == args[0]:
                    ins.append(objs[o])
            print(ins)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update command to update an instance based on the class name and id
        """
        obj = self.find_obj(arg)
        protected = ["id", "created_at", "updated_at"]
        if obj:
            args = split(arg, " ")
            objs = storage.all()
            if len(args) < 3:
                print('** attribute name missing **')
            elif len(args) < 4:
                print('** value missing **')
            elif args[2] not in protected:
                obj.__dict__[args[2]] = args[3]
                obj.updated_at = datetime.now()
                storage.save()

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        quit()

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        quit()

    def do_help(self, arg):
        """
        Help command to get info on specified command
        If no parameter given list all commands
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """
        Empty line does nothing
        """
        return

    def count(self, arg):
        """
        Counts the number of instances of a class
        """
        objs = storage.all()
        ins = []
        count = 0
        if arg in self.vc:
            for o in objs:
                if o[0:len(arg)] == arg:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """
        Happens if command prefix is not recognized
        """
        command = line.split(".")
        if len(command) >= 2:
            if command[1][:-2] == "all":
                self.do_all(command[0])
            elif command[1][:-2] == "count":
                self.count(command[0])
        else:
            cmd.Cmd.default(self, line)

    def find_obj(self, arg):
        """
        Finds specified object instance based on given arguments
        """
        if not arg:
            print('** class name missing **')
            return
        args = arg.split(" ")
        objs = storage.all()
        if args[0] in self.vc:
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_name = args[0] + "." + args[1]
            if obj_name not in objs:
                print("** no instance found **")
            else:
                return objs[obj_name]
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
