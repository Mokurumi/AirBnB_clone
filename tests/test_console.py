#!/usr/bin/python3
"""
This modulle describes tests for command interpretter
"""


import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    This class tests the command interpretter functionality
    """
    def test_help(self):
        """
        Test the 'help' command.
        It should print the list of documented commands.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertTrue(
                    "Documented commands (type help <topic>):" in f.getvalue()
                    )

    def test_create(self):
        """
        Test the 'create' command.
        It should create a new instance of the specified class
            and print its ID.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            # Check if the ID was generated
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_create_missing_class(self):
        """
        Test 'create' with a missing class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertTrue("** class name missing **" in f.getvalue())

    def test_create_invalid_class(self):
        """
        Test 'create' with an invalid class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create SomeInvalidClass")
            self.assertTrue("** class doesn't exist **" in f.getvalue())

    def test_show(self):
        """
        Test the 'show' command.
        It should show information about an instance based on its class and ID.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {created_id}")
            self.assertTrue(f"BaseModel" in f.getvalue())

    def test_show_missing_class(self):
        """
        Test 'show' with a missing class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertTrue("** class name missing **" in f.getvalue())

    def test_show_missing_id(self):
        """
        Test 'show' with a missing ID.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertTrue("** instance id missing **" in f.getvalue())

    def test_show_invalid_class(self):
        """
        Test 'show' with an invalid class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show SomeInvalidClass 1234")
            self.assertTrue("** class doesn't exist **" in f.getvalue())

    def test_show_no_instance(self):
        """
        Test 'show' with a non-existing instance.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertTrue("** no instance found **" in f.getvalue())

    def test_destroy(self):
        """
        Test the 'destroy' command.
        It should delete an instance based on its class and ID.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {created_id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {created_id}")
            self.assertTrue("** no instance found **" in f.getvalue())

    def test_destroy_missing_class(self):
        """
        Test 'destroy' with a missing class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertTrue("** class name missing **" in f.getvalue())

    def test_destroy_missing_id(self):
        """
        Test 'destroy' with a missing ID.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertTrue("** instance id missing **" in f.getvalue())

    def test_destroy_invalid_class(self):
        """
        Test 'destroy' with an invalid class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy SomeInvalidClass 1234")
            self.assertTrue("** class doesn't exist **" in f.getvalue())

    def test_destroy_no_instance(self):
        """
        Test 'destroy' with a non-existing instance.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertTrue("** no instance found **" in f.getvalue())

    def test_all(self):
        """
        Test the 'all' command.
        It should show all instances of a class or
            all instances if no class name is specified.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue("BaseModel" in f.getvalue())

    def test_all_missing_class(self):
        """
        Test 'all' with a missing class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertTrue("** class name missing **" in f.getvalue())

    def test_all_invalid_class(self):
        """
        Test 'all' with an invalid class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all SomeInvalidClass")
            self.assertTrue("** class doesn't exist **" in f.getvalue())

    def test_update(self):
        """
        Test the 'update' command.
        It should update an attribute of an instance based on its class, ID,
            attribute name, and attribute value.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {created_id} name 'NewName'")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {created_id}")
            self.assertTrue("NewName" in f.getvalue())

    def test_update_missing_class(self):
        """
        Test 'update' with a missing class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertTrue("** class name missing **" in f.getvalue())

    def test_update_missing_id(self):
        """
        Test 'update' with a missing ID.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertTrue("** instance id missing **" in f.getvalue())

    def test_update_invalid_class(self):
        """
        Test 'update' with an invalid class name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update SomeInvalidClass 1234 name 'NewName'")
            self.assertTrue("** class doesn't exist **" in f.getvalue())

    def test_update_no_instance(self):
        """
        Test 'update' with a non-existing instance.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234 name 'NewName'")
            self.assertTrue("** no instance found **" in f.getvalue())

    def test_update_missing_attr_name(self):
        """
        Test 'update' with a missing attribute name.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {created_id}")
            self.assertTrue("** attribute name missing **" in f.getvalue())

    def test_update_missing_value(self):
        """
        Test 'update' with a missing value.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {created_id} name")
            self.assertTrue("** value missing **" in f.getvalue())

    def test_update_invalid_dict_format(self):
        """
        Test 'update' with an invalid dictionary format.
        It should print an error message.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {created_id} name {123}")
            self.assertTrue("** invalid dictionary format **" in f.getvalue())

    def test_update_with_dict(self):
        """
        Test 'update' with a dictionary representation.
        It should update the instance using the dictionary.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    f"update BaseModel {created_id} {'{'name': 'NewName'}'}"
                    )
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {created_id}")
            self.assertTrue("NewName" in f.getvalue())

    def test_update_with_dict_multiple_attrs(self):
        """
        Test 'update' with a dictionary containing multiple attributes.
        It should update the instance with multiple attributes.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
            f"update BaseModel {created_id} {'{'name': 'NewName', 'age': 30}'}"
                    )
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {created_id}")
            output = f.getvalue()
            self.assertTrue("NewName" in output)
            self.assertTrue("30" in output)


if __name__ == '__main__':
    unittest.main()
