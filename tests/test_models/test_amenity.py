<<<<<<< HEAD

import sys
import unittest
from datetime import datetime
from io import StringIO

import pycodestyle
from models import amenity
from tests.test_models.test_base_model import BaseModel

Amenity = amenity.Amenity


class TestAmenityDocsAndStyle(unittest.TestCase):
    """Tests Amenity class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/amenity.py", "tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(amenity.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(Amenity.__name__, "Amenity")


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity Class"""

    def setUp(self):
        """creates a test object for other tests"""
        self.test_obj = Amenity()
        self.test_obj.name = "example"

    def test_amenity_is_subclass_of_base_model(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_public_attributes_exist(self):
        """tests wether the public instance attributes exist."""
        req_att = ["id", "created_at", "updated_at", "name"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_public_attributes_have_correct_type(self):
        """tests wether the public instance attributes exist."""
        req_att = ["name"]
        for attrib in req_att:
            self.assertTrue(type(getattr(self.test_obj, attrib)), str)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print [<class name>] (<self.id>) <self.__dict__>"""
        self.test_obj.my_number = 89
        cls_name = Amenity.__name__
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
                         Amenity.__name__)

    def test_init_with_kwargs(self):
        """test that Amenity can be constructed from kwargs"""
        temp_obj_2 = Amenity(**self.test_obj.to_dict())

        for k, v in self.test_obj.__dict__.items():
            self.assertEqual(v, temp_obj_2.__dict__[k])


if __name__ == "__main__":
    unittest.main()
=======
#!/usr/bin/python3
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


class TestAmenityDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)


class TestAmenityPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestAmenity(unittest.TestCase):
    """ tests for class Amenity """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.amenity = Amenity()

    def test_subclass(self):
        """ test that amenity is a subclass of basemodel """
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.amenity.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.amenity.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.amenity.updated_at))

    def test_name(self):
        """ test name """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.amenity.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.amenity))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
