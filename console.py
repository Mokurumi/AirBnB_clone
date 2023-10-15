#!/usr/bin/python3
"""
This module contains the console program
The console program serves as an entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User  # Import the User class


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class_name>
        """
        class_name = arg.split()[0]
        if class_name not in globals():
            print("* class doesn't exist *")
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
        if len(args) == 0:
            print("* class name missing *")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("* class doesn't exist *")
            elif len(args) < 2:
                print("* instance id missing *")
            else:
                id = args[1]
                key = class_name + "." + id
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("* no instance found *")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
            (saves the change to the JSON file).
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("* class name missing *")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("* class doesn't exist *")
            elif len(args) < 2:
                print("* instance id missing *")
            else:
                id = args[1]
                key = class_name + "." + id
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("* no instance found *")

    def do_all(self, arg):
        """
        Shows all instances of a class or
            all instances if no class name is specified.
        Usage: all [class_name]
        """
        class_name = arg if arg else None
        if class_name is not None and class_name not in globals():
            print("* class doesn't exist *")
            return
        all_instances = []
        for key, value in storage.all().items():
            if class_name is None or key.split('.')[0] == class_name:
                all_instances.append(str(value))
        print(all_instances)

    def do_update(self, arg):
        """
        Updates an attribute of an instance based on its class and ID.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("* class name missing *")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("* class doesn't exist *")
            elif len(args) < 2:
                print("* instance id missing *")
            elif len(args) < 3:
                print("* attribute name missing *")
            elif len(args) < 4:
                print("* value missing *")
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
                    print("* no instance found *")

    def emptyline(self):
        pass

    # Include commands for the 'User' class
    def do_create_user(self, arg):
        """
        Creates a new instance of User, saves it, and prints the id.
        Usage: create User
        """
        new_instance = User()
        new_instance.save()
        print(new_instance.id)

    def do_show_user(self, arg):
        """
        Shows information about a User instance based on its ID.
        Usage: show User <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("* instance id missing *")
        else:
            id = args[0]
            key = "User." + id
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("* no instance found *")

    def do_destroy_user(self, arg):
        """
        Deletes a User instance based on its ID
            (saves the change to the JSON file).
        Usage: destroy User <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("* instance id missing *")
        else:
            id = args[0]
            key = "User." + id
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("* no instance found *")

    def do_all_user(self, arg):
        """
        Shows all User instances.
        Usage: all User
        """
        all_instances = []
        for key, value in storage.all().items():
            if key.startswith("User."):
                all_instances.append(str(value))
        print(all_instances)

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

if name == 'main':
    HBNBCommand().cmdloop()
