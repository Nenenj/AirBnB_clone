#!/usr/bin/python3
<<<<<<< HEAD
"""Module test_place

This Module contains a tests for Place Class
"""

import sys
import unittest
import uuid
from datetime import datetime
from io import StringIO

import pycodestyle
from models import place
from tests.test_models.test_base_model import BaseModel

Place = place.Place


class TestPlaceDocsAndStyle(unittest.TestCase):
    """Tests Place class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/place.py", "tests/test_models/test_place.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(place.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(Place.__name__, "Place")


class TestPlace(unittest.TestCase):
    """Test cases for Place Class"""

    def setUp(self):
        """creates a test object for other tests"""
        self.test_obj = Place()
        self.test_obj.city_id = str(uuid.uuid4())
        self.test_obj.user_id = str(uuid.uuid4())
        self.test_obj.name = "some place"
        self.test_obj.description = "example description"
        self.test_obj.number_rooms = 3
        self.test_obj.number_bathrooms = 3
        self.test_obj.max_guest = 3
        self.test_obj.price_by_night = 3
        self.test_obj.latitude = 10.56
        self.test_obj.longitude = 34.34
        self.test_obj.amenity_ids = [
            str(uuid.uuid4()), str(uuid.uuid4())
        ]

    def test_place_is_subclass_of_base_model(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_public_attributes_exist(self):
        """tests wether the public instance attributes exist."""
        req_att = ["id", "created_at", "updated_at",
                   "city_id", "user_id", "name", "description", "number_rooms",
                   "number_bathrooms", "max_guest", "price_by_night",
                   "latitude", "longitude", "amenity_ids"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_public_attributes_have_correct_type(self):
        """tests wether the public instance attributes exist."""
        req_att_s = ["city_id", "user_id", "name", "description"]
        for attrib in req_att_s:
            self.assertTrue(type(getattr(self.test_obj, attrib)), str)
        req_att_i = ["number_rooms", "number_bathrooms", "max_guest",
                     "price_by_night"]
        for attrib in req_att_i:
            self.assertTrue(type(getattr(self.test_obj, attrib)), int)
        req_att_f = ["latitude", "longitude"]
        for attrib in req_att_f:
            self.assertTrue(type(getattr(self.test_obj, attrib)), float)

        self.assertTrue(type(getattr(self.test_obj, "amenity_ids")), list)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print [<class name>] (<self.id>) <self.__dict__>"""
        self.test_obj.my_number = 89
        cls_name = Place.__name__
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
                         Place.__name__)

    def test_init_with_kwargs(self):
        """test that Place can be constructed from kwargs"""
        temp_obj_2 = Place(**self.test_obj.to_dict())

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


class TestPlaceDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Place.__doc__) > 0)


class TestPlacePep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestPlace(unittest.TestCase):
    """ tests for class Place """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.place = Place()

    def test_subclass(self):
        """ test that place is a subclass of basemodel """
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.place.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.place.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.place.updated_at))

    def test_city_id(self):
        """ test city_id """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """ test user_id """
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """ test name """
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """ test description """
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """ test number_rooms """
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """ test number_bathrooms """
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """ test max_guest """
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """ test price_by_night """
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """ test latitude """
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """ test longitude """
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """ test amenity_ids """
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.place.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.place))

    def test_str(self):
        """ test ___str___ method """
        correct = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(correct, str(self.place))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
