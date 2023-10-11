#!/usr/bin/python3
"""
This module contains the console program
The console program serves as an entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg
            if class_name not in globals():
                print("** class doesn't exist **")
            else:
                new_instance = globals()[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
            based on the class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                id = args[1]
                key = class_name + "." + id
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
            (saves the change to the JSON file).
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                id = args[1]
                key = class_name + "." + id
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances
            based on the class name (or all instances).
        Usage: all [class_name]
        """
        class_name = arg if arg else None
        if class_name is not None and class_name not in globals():
            print("** class doesn't exist **")
            return
        all_instances = []
        for key, value in storage.all().items():
            if class_name is None or key.split('.')[0] == class_name:
                all_instances.append(str(value))
        print(all_instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
            id by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                id = args[1]
                key = class_name + "." + id
                if key in storage.all():
                    instance = storage.all()[key]
                    attr_name = args[2]
                    attr_value = args[3].strip("\"")
                    setattr(instance, attr_name, attr_value)
                    instance.save()
                else:
                    print("** no instance found **")

    def emptyline(self):
        pass

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
