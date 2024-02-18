#!/usr/bin/python3
<<<<<<< HEAD
"""Module test_user

This Module contains a tests for User Class
"""

import inspect
import sys
import unittest
from datetime import datetime
from io import StringIO

import pycodestyle
from models import user
from tests.test_models.test_base_model import BaseModel

User = user.User


class TestUserDocsAndStyle(unittest.TestCase):
    """Tests User class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/user.py", "tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(user.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(User.__name__, "User")


class TestUser(unittest.TestCase):
    """Test cases for User Class"""

    def setUp(self):
        """creates a test object for other tests"""
        self.test_obj = User()
        self.test_obj.email = "test@example.com"
        self.test_obj.password = "p@$$w0rd"
        self.test_obj.first_name = "John"
        self.test_obj.last_name = "Doe"

    def test_user_is_subclass_of_base_model(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_public_attributes_exist(self):
        """tests wether the public instance attributes exist."""
        req_att = ["id", "created_at", "updated_at",
                   "email", "password", "first_name", "last_name"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_public_attributes_have_correct_type(self):
        """tests wether the public instance attributes exist."""
        req_att = ["email", "password", "first_name", "last_name"]
        for attrib in req_att:
            self.assertTrue(type(getattr(self.test_obj, attrib)), str)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print [<class name>] (<self.id>) <self.__dict__>"""
        self.test_obj.my_number = 89
        cls_name = User.__name__
        id = self.test_obj.id
        expected = f"[{cls_name}] ({id}) {self.test_obj.__dict__}"
        output = StringIO()
        sys.stdout = output
        print(self.test_obj)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue().strip("\n"), expected)

    def test_to_dict_returns_a_dictionary_of_attributes(self):
        """to_dict should return a dictionary containing all key/value of
        self.__dict__
        """
        temp_dict = self.test_obj.to_dict()
        self.assertIsInstance(temp_dict, dict)
        keys = temp_dict.keys()

        for k, v in self.test_obj.__dict__.items():
            self.assertIn(k, keys)
            if not isinstance(self.test_obj.__dict__[k], datetime):
                self.assertEqual(temp_dict[k], v)

    def test_to_dict_has_a_key_with_the_class_name(self):
        """to_dict must have a key of __class__ with a value of the classes
        name
        """
        temp_dict = self.test_obj.to_dict()
        self.assertIn("__class__", temp_dict.keys())
        self.assertEqual(temp_dict["__class__"],
                         User.__name__)

    def test_init_with_kwargs(self):
        """test that User can be constructed from kwargs"""
        temp_obj_2 = User(**self.test_obj.to_dict())

        for k, v in self.test_obj.__dict__.items():
            self.assertEqual(v, temp_obj_2.__dict__[k])


if __name__ == "__main__":
    unittest.main()
=======
import unittest
import pep8
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestUserDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(User.__doc__) > 0)


class TestUserPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestUser(unittest.TestCase):
    """ tests for class User """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.user = User()

    def test_subclass(self):
        """ test that user is a subclass of basemodel """
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.user.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.user.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.user.updated_at))

    def test_email(self):
        """ test email """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")

    def test_password(self):
        """ test password """
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        """ test first_name """
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        """ test last_name """
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.user.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.user))

    def test_str(self):
        """ test ___str___ method """
        correct = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(correct, str(self.user))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
