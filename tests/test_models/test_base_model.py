#!/usr/bin/python3
"""defines unittests basemodel"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """unittests testing BaseModel class."""

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

    def test_email_is_public_str(self):
        self.assertEqual(str, type(BaseModel.email))

    def twoBaseModelsIdUnique(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, user2.id)

    def twobasemodelsDifferentCreatTime(self):
        basemodel1 = BaseModel()
        sleep(0.1)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.created_at, user2.created_at)

    def twoBaseModelsDifferentUpdateTime(self):
        basemodel1 = BaseModel()
        sleep(0.1)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.updated_at, user2.updated_at)

    def stringRepTest(self):
        date = datetime.today()
        dateRepr = repr(date)
        basemodel = BaseModel()
        basemodel.id = "012345"
        basemodel.created_at = user.updated_at = date
        basemodelStr = user.__str__()
        self.assertIn("[BaseModel] (abcde)", basemodelstr)
        self.assertIn("'id': '012345'", basemodelstr)
        self.assertIn("'created_at': " + dateRepr, basemodelStr)
        self.assertIn("'updated_at': " + dateRepr, basemodelStr)

    def unusedArgsTest(self):
        basemodel = BaseModel(None)
        self.assertNotIn(None, basemodel.__dict__.values())

    def kwargsInstalTest(self):
        date = datetime.today()
        date_iso = date.isoformat()
        basemodel = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(us.id, "000000")
        self.assertEqual(us.created_at, date)
        self.assertEqual(us.updated_at, date)

    def noKwargsInstalTest(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
