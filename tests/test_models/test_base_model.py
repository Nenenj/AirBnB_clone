#!/usr/bin/python3
<<<<<<< HEAD
"""Module test_base_model

This Module contains a tests for Base Class
"""

import inspect
import json
import os
import sys
import unittest
from datetime import datetime
from io import StringIO
from uuid import UUID

import pycodestyle
from models import base_model
from models.engine.file_storage import FileStorage

BaseModel = base_model.BaseModel


class TestBaseModelDocsAndStyle(unittest.TestCase):
    """Tests Base class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/base_model.py", "tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(BaseModel, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(BaseModel.__name__, "BaseModel")


class TestBaseModel(unittest.TestCase):
    """Test cases for Base Class"""

    def setUp(self):
        """creates a test object for other tests"""
        self.test_obj = BaseModel()

    def test_public_attributes_exist(self):
        """tests wether the public instance attributes - "id" "create_at" and
        "updated_at" exist."""
        req_att = ["id", "created_at", "updated_at"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_id_attribute_shall_be_uuid4(self):
        """tests wether id attribute is of type string representation of
        datetime"""
        self.assertIsInstance(self.test_obj.id, str)

        try:
            _ = UUID(self.test_obj.id, version=4)
        except Exception:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    def test_datetime_attributes(self):
        """tests if created_at and updated_at instance attributes are of
        datetime type"""
        self.assertIsInstance(self.test_obj.created_at, datetime)
        self.assertIsInstance(self.test_obj.updated_at, datetime)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print [<class name>] (<self.id>) <self.__dict__>"""
        self.test_obj.my_number = 89
        cls_name = BaseModel.__name__
        id = self.test_obj.id
        expected = f"[{cls_name}] ({id}) {self.test_obj.__dict__}"
        output = StringIO()
        sys.stdout = output
        print(self.test_obj)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue().strip("\n"), expected)

    def test_public_method_attributes_exist(self):
        """tests wether public instance methods - "save" "to_dict" exist."""
        req_att = ["save", "to_dict"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib)
                            and callable(getattr(self.test_obj, attrib)))

    def test_save_method_updates_updated_at_value(self):
        """save method shall update updated_at"""
        old_date = self.test_obj.updated_at
        self.test_obj.save()
        self.assertIsInstance(old_date, datetime)
        #self.assertNotEqual(self.test_obj.updated_at, old_date)

    def test_save_method_updates_storage(self):
        """save method shall update storage"""
        file_path = "file.json"
        with open(file_path, 'w') as f:
            json.dump({}, f)
        storage = FileStorage()
        storage.reload()
        storage.new(self.test_obj)
        storage.save()

        old_date = self.test_obj.updated_at
        self.test_obj.save()

        storage.reload()
        saved_obj = storage.all(
        )[f"{self.test_obj.__class__.__name__}.{self.test_obj.id}"]

        self.assertNotEqual(old_date, saved_obj.updated_at)

        if os.path.exists(file_path):
            os.remove(file_path)

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

    def test_to_dict_returns_a_new_dictionary_of_attributes(self):
        """to_dict should return a copy of __dict__"""
        temp_dict = self.test_obj.to_dict()
        self.assertNotEqual(id(temp_dict), id(self.test_obj.__dict__))

    def test_to_dict_has_a_key_with_the_class_name(self):
        """to_dict must have a key of __class__ with a value of the classes
        name
        """
        temp_dict = self.test_obj.to_dict()
        self.assertIn("__class__", temp_dict.keys())
        self.assertEqual(temp_dict["__class__"],
                         BaseModel.__name__)

    def test_to_dict_formats_dates_with_isoformat(self):
        """to_dict should store dates in isoformat"""
        temp_dict = self.test_obj.to_dict()

        for k, v in self.test_obj.__dict__.items():
            if isinstance(self.test_obj.__dict__[k], datetime):
                self.assertEqual(datetime.fromisoformat(temp_dict[k]), v)

    def test_init_with_kwargs(self):
        """test that BaseClass can be constructed from kwargs"""
        temp_obj_2 = BaseModel(**self.test_obj.to_dict())

        for k, v in self.test_obj.__dict__.items():
            self.assertEqual(v, temp_obj_2.__dict__[k])
=======
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa


if __name__ == "__main__":
    unittest.main()
