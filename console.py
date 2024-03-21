#!/usr/bin/python3
"""Module that defines the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """The command interpreter class which inherists from cmd"""

    # Custom promt
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command which exits the program"""
        return True

    def do_EOF(self, arg):
        """EOF command prints empty line, exits the program"""
        print()
        return True

    def emptyline(self):
        """Empty line and enter do nothing"""
        pass

    def do_create(self, class_name):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """

        if class_name == "":
            print("** class name missing **")
        else:
            try:
                obj = globals()[class_name]()
                obj.save()
                print(obj.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, name_and_id):
        """Prints the string representation of an instance based on the class name and id"""

        if name_and_id == "":
            print("** class name missing **")
        elif name_and_id.split()[0] not in globals().keys():
            print("** class doesn't exist **")
        elif name_and_id:
            try:
                class_name, class_id = name_and_id.split()
            except ValueError:
                print("** instance id missing **")
        else:
            if f"{class_name}.{class_id}" in storage._FileStorage__objects:
                print(
                    storage._FileStorage__objects[f"{class_name}.{class_id}"])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
