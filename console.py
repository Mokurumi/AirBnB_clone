#!/usr/bin/python3
"""
This module contains the console program
The console program serves as an entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # Define the supported classes
    supported_classes = {
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def _create_instance(self, class_name):
        """
        Creates a new instance of the specified class, saves it, and prints the ID.
        """
        if class_name not in self.supported_classes:
            print("* class doesn't exist *")
            return
        new_instance = self.supported_classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_create(self, arg):
        """
        Creates a new instance of the specified class, saves it, and prints the ID.
        Usage: create <class_name>
        """
        if not arg:
            print("* class name missing *")
        else:
            self._create_instance(arg.split()[0])

    def do_show(self, arg):
        """
        Prints the string representation of an instance
            based on the class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("* class name missing *")
            return
        class_name = args[0]
        if class_name not in self.supported_classes:
            print("* class doesn't exist *")
            return

        if len(args) < 2:
            print("* instance id missing *")
            return
        id = args[1]
        key = class_name + "." + id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("* no instance found *")

    def do_destroy(self, arg):
        """
        Deletes an instance based on its class and ID (saves the change to the JSON file).
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("* class name missing *")
            return
        class_name = args[0]
        if class_name not in self.supported_classes:
            print("* class doesn't exist *")
            return

        if len(args) < 2:
            print("* instance id missing *")
            return
        id = args[1]
        key = class_name + "." + id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("* no instance found *")

    def do_all(self, arg):
        """
        Shows all instances of a class or all instances if no class name is specified.
        Usage: all [class_name]
        """
        class_name = arg if arg else None
        if class_name is not None and class_name not in self.supported_classes:
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
        if not args:
            print("* class name missing *")
            return
        class_name = args[0]
        if class_name not in self.supported_classes:
            print("* class doesn't exist *")
            return

        if len(args) < 2:
            print("* instance id missing *")
            return

        id = args[1]
        key = class_name + "." + id
        if key not in storage.all():
            print("* no instance found *")
            return

        if len(args) < 3:
            print("* attribute name missing *")
            return

        if len(args) < 4:
            print("* value missing *")
            return

        attr_name = args[2]
        attr_value = args[3].strip("\"")
        instance = storage.all()[key]
        setattr(instance, attr_name, attr_value)
        instance.save()

    def emptyline(self):
        """
        Do nothing if the line is empty
        """
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
