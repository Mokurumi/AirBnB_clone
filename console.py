#!/usr/bin/python3
"""
This module contains the console program
The console program serves as an entry point of the command interpreter
"""


import cmd
import json
import importlib
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This is the entry point of the command interpretter
    it has functions to process different commands
    """
    prompt = "(hbnb) "
    valid_class_names = [
            "BaseModel",
            "User",
            "City",
            "State",
            "Amenity",
            "Place",
            "Review"
            ]

    def check_valid_class(self, class_name):
        """
        Checks if class name provided is in the list
        """
        if class_name not in self.valid_class_names:
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, arg):
        """
        Creates a new instance of the specified class, saves it,
            and prints the ID.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Shows information about an instance based on its class and ID.
        Usage: <class_name>.show(<id>)
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        if self.check_valid_class(class_name):
            try:
                obj = storage.all()[f"{class_name}.{obj_id}"]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on its class and ID
            (saves the change to the JSON file).
        Usage: <class_name>.destroy(<id>)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if not self.check_valid_class(class_name):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        
        try:
            key = f"{class_name}.{obj_id}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except KeyError:
            print("** no instance found **")


    def do_all(self, arg):
        """
        Prints all string representations of all instances based or
            not on the class name.
        Usage: all [class name]
        """
        args = arg.split()
        obj_list = []
        if len(args) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in self.valid_class_names:
                print("** class doesn't exist **")
                return
            try:
                for obj in storage.all().values():
                    if obj.__class__.__name__ == class_name:
                        obj_list.append(str(obj))
            except KeyError:
                print("** class doesn't exist **")
                return
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on its class, ID,
            and a dictionary representation.
        Usage: <class_name>.update(<id>, <dictionary_representation>)
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        if self.check_valid_class(class_name):
            try:
                obj = storage.all()[f"{class_name}.{obj_id}"]
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
                if len(args) == 3:
                    print("** value missing **")
                    return
                attribute_name = args[2]
                if args[3].startswith('"') and args[3].endswith('"'):
                    attribute_value = args[3][1:-1]
                else:
                    attribute_value = args[3]
                setattr(obj, attribute_name, attribute_value)
                obj.save()
            except KeyError:
                print("** no instance found **")

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class.
        Usage: <class_name>.count()
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            count = sum(1 for obj in storage.all().values()
                        if obj.__class__.__name__ == class_name)
            print(count)

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
        """Exit the command interpreter using EOF (Ctrl-D)"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
