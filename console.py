#!/usr/bin/python3
"""Module that defines the command interpreter"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
