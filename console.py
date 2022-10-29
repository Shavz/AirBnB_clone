#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
import json

from shlex import split

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Hbnb class definition
    """

    prompt = '(hbnb) '
    file = None
    __classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }

    __commands = {
        "show",
        "count",
        "all",
        "destroy",
        "update"
    }

    def do_count(self, argv):
        """
        Count the amount of instances in a given class
        """
        l_c = argv.split()
        all_instances = storage.all()
        if l_c[0] in self.__classes:
            num = 0
            for k, ob in all_instances.items():
                if l_c[0] in k:
                    num = num + 1
            print(num)
        else:
            print("** class doesn't exist **")

    def help_count(self):
        """
        Help command for count
        """

        msg = "Count the amount of instances in a given class\n"
        print(msg)

    def emptyline(self):
        """
        Empty line
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """

        quit()
        return True

    def help_quit(self):
        """
        Help command for quitting the program
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        print()
        return True

    def help_EOF(self):
        """
        Help command for EOF
        """
        print("EOF command to exit the program\n")

    def do_create(self, arg):
        """
        Create a BaseModel and save json in a file
        """

        if len(arg) > 0:
            list_arg = arg.split()
            if list_arg[0] in HBNBCommand.__classes:
                print(eval(list_arg[0])().id)
                storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """
        Help command for create
        """
        print("Create a BaseModel and save json in a file\n")

    def do_show(self, arg):
        """
        Print the string representation of an instance
        based on the class name and id
        """

        if len(arg) > 0:
            list_arg = arg.split()
            objects = storage.all()
            if len(list_arg) >= 2:
                clsId = list_arg[0] + '.' + list_arg[1]
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    print(objects[clsId])
                else:
                    print("** no instance found **")
            else:
                if len(list_arg) == 1:
                    objs_cls = [e.split('.')[0] for e in list(objects.keys())]
                    if arg not in objs_cls:
                        print("** class doesn't exist **")
                    else:
                        print("** instance id missing **")
        else:
            print("** class name missing **")

    def help_show(self):
        """
        Help command
        """

        msg = "Prints the string representation of an instance "
        msg += "based on the class name and id\n"
        print(msg)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """

        if len(arg) > 0:
            list_arg = arg.split()
            objects = storage.all()
            if len(list_arg) >= 2:
                clsId = list_arg[0] + '.' + list_arg[1]
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    del objects[clsId]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                if len(list_arg) == 1:
                    objs_cls = [e.split('.')[0] for e in list(objects.keys())]
                    if arg not in objs_cls:
                        print("** class doesn't exist **")
                    else:
                        print("** instance id missing **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """
        Help command to destroy
        """
        print("Deletes an instance based on the class name and id\n")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based on the class name
        """

        objects = storage.all()
        if len(arg) > 0:
            list_arg = arg.split()
            clsObjs = [str(v) for k, v in objects.items()
                       if list_arg[0] == k.split('.')[0]]
            if len(clsObjs) > 0:
                print(clsObjs)
            else:
                print("** class doesn't exist **")
        else:
            allObjs = [str(v) for k, v in objects.items()]
            print(allObjs)

    def help_all(self):
        """
        Help command
        """

        msg = "Prints all string representation of all instances "
        msg += "based or not on the class name\n"
        print(msg)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """

        if len(arg) > 0:
            objects = storage.all()
            list_arg = split(arg)
            if len(list_arg) == 1:
                clsObjs = [str(v) for k, v in objects.items()
                           if arg == k.split('.')[0]]
                if len(clsObjs) > 0:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(list_arg) == 2:
                clsId = '.'.join(list_arg)
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            elif len(list_arg) == 3:
                clsId = list_arg[0] + '.' + list_arg[1]
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    if list_arg[2]:
                        print("** value missing **")
                else:
                    print("** no instance found **")
            else:
                clsId = list_arg[0] + '.' + list_arg[1]
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    if list_arg[2]:
                        obj = objects[clsId]
                        if HBNBCommand.RepresentsInt(list_arg[3]):
                            setattr(obj, list_arg[2], int(list_arg[3]))
                        elif HBNBCommand.RepresentsFloat(list_arg[3]):
                            setattr(obj, list_arg[2], float(list_arg[3]))
                        else:
                            setattr(obj, list_arg[2], list_arg[3])
                        obj.save()
                    else:
                        print("** value missing **")
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def help_update(self):
        """
        Help command for updating
        """

        msg = "Updates an instance based on the class "
        msg += "name and id by adding or updating attribute\n"
        msg += "Usage: update <class name> <id> <attribute name>  "
        msg += "\"<attribute value>\"\n"
        print(msg)

    @staticmethod
    def RepresentsInt(str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    @staticmethod
    def RepresentsFloat(str):
        try:
            float(str)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
