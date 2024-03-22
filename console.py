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
        """Prints the string representation of an instance
           based on the class name and id
        """

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

        saved = storage.all()
        class_list = []
        obj_list = []

        # Extract class names from saved keys
        for key in saved.keys():
            class_name = key.split(".")[0]
            class_list.append(class_name)

        if not line:
            # Print string representation of all available instances
            for obj in saved.values():
                obj_list.append(str(obj))
            print(obj_list)

        else:
            # If line is not empty, check if specified class exists
            if line in class_list:
                # Print string rep of instances of the specified class
                for obj in saved.values():
                    if obj.__class__.__name__ == line:
                        obj_list.append(str(obj))
                print(obj_list)
            else:
                # If line is not in our class list, print error message
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
           by adding or updating the attributes
        """

        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in globals().keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = f"{class_name}.{obj_id}"

        if obj_key not in storage._FileStorage__objects:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = " ".join(args[3:])


        # Warn user not to update non-simple attributes
        if attr_name in ["id", "created_at", "updated_at"]:
            print(" can't update id, created_at, or updated_at")
            return

        # If everything is fine, get the object from storage
        obj = storage._FileStorage__objects[obj_key]

        # Try to evaluate the value the user provided for attribute
        try:
            attr_value = eval(attr_value)
        except Exception as e:
            print("** value missing **")
            return

        # Set the provided attribute value for the object
        setattr(obj, attr_name, attr_value)

        # Save the updated object to the storage
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
