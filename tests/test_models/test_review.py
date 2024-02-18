#!/usr/bin/python3
<<<<<<< HEAD
"""Module test_review

This Module contains a tests for Review Class
"""

import sys
import unittest
import uuid
from datetime import datetime
from io import StringIO

import pycodestyle
from models import review
from tests.test_models.test_base_model import BaseModel

Review = review.Review


class TestReviewDocsAndStyle(unittest.TestCase):
    """Tests Review class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/review.py", "tests/test_models/test_review.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(review.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(Review.__name__, "Review")


class TestReview(unittest.TestCase):
    """Test cases for Review Class"""

    def setUp(self):
        """creates a test object for other tests"""
        self.test_obj = Review()
        self.test_obj.place_id = str(uuid.uuid4())
        self.test_obj.user_id = str(uuid.uuid4())
        self.test_obj.text = "fantastic review"

    def test_review_is_subclass_of_base_model(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_public_attributes_exist(self):
        """tests wether the public instance attributes exist."""
        req_att = ["id", "created_at", "updated_at",
                   "place_id", "user_id", "text"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_public_attributes_have_correct_type(self):
        """tests wether the public instance attributes exist."""
        req_att = ["place_id", "user_id", "text"]
        for attrib in req_att:
            self.assertTrue(type(getattr(self.test_obj, attrib)), str)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print [<class name>] (<self.id>) <self.__dict__>"""
        self.test_obj.my_number = 89
        cls_name = Review.__name__
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
                         Review.__name__)

    def test_init_with_kwargs(self):
        """test that Review can be constructed from kwargs"""
        temp_obj_2 = Review(**self.test_obj.to_dict())

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


class TestReviewDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Review.__doc__) > 0)


class TestReviewPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestReview(unittest.TestCase):
    """ tests for class Review """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.review = Review()

    def test_subclass(self):
        """ test that review is a subclass of basemodel """
        self.assertIsInstance(self.review, BaseModel)
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.review.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.review.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.review.updated_at))

    def test_place_id(self):
        """ test place_id """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """ test user_id """
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """ test text """
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.review.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.review))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
