#!/usr/bin/python3
"""
This module contains the console program
The console program serves as an entry point of the command interpreter
"""


import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the entry point of the command interpretter
    it has functions to process different commands
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of the specified class, saves it,
            and prints the ID.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_instance = storage.classes()[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """
        Shows information about an instance based on its class and ID.
        Usage: <class_name>.show(<id>)
        """
        args = arg.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on its class and ID
            (saves the change to the JSON file).
        Usage: <class_name>.destroy(<id>)
        """
        args = arg.split(' ')
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
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
        args = arg.split(' ')
        if len(args) == 0:
            print([str(obj) for obj in storage.all().items()])
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(obj) for key, obj in storage.all().items()
                       if key.startswith(class_name)])


    def do_update(self, arg):
        """
        Updates an instance based on its class, ID,
            and a dictionary representation.
        Usage: <class_name>.update(<id>, <dictionary_representation>)
        """
        args = arg.split(' ')
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3].strip('"')
                    instance = storage.all()[key]
                    setattr(instance, attribute_name, attribute_value)
                    storage.save()

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
