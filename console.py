#!/usr/bin/python3
"""
This module contains the console program
The console program serves as an entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with EOF (Ctrl-D)
        """
        return True

if _name_ == '_main_':
    HBNBCommand().cmdloop()
