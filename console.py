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
        elif len(name_and_id.split()) == 2:
            class_name, class_id = name_and_id.split()

            if f"{class_name}.{class_id}" in storage._FileStorage__objects:
                print(
                    storage._FileStorage__objects[f"{class_name}.{class_id}"])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, name_and_id):
        """Deletes an instance based on name and ID, saves changes"""

        if name_and_id == "":
            print("** class name missing **")
        elif name_and_id.split()[0] not in globals().keys():
            print("** class doesn't exist **")
        elif len(name_and_id.split()) == 2:
            class_name, class_id = name_and_id.split()

            if f"{class_name}.{class_id}" in storage._FileStorage__objects:
                del (storage._FileStorage__objects[f"{class_name}.{class_id}"])
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, line):
        """Prints string representations of all available objects"""
        obj_list = []
        class_list = []
        for key in storage.all().keys():
            class_list.append(key.split(".")[0])
        if line != "":
            if line not in class_list:
                print("** class doesn't exist **")
            else:
                print(str(class_list))

        else:
            saved = storage.all()
            for objs in saved.values():
                obj_list.append(str(objs))
                print(objs)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
