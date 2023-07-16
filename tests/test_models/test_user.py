#!/usr/bin/python3
"""defines unittests user"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """unittests testing User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def twoUsersIdUnique(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def twousersDifferentCreatTime(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def twoUsersDifferentUpdateTime(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def stringRepTest(self):
        date = datetime.today()
        dateRepr = repr(date)
        user = User()
        user.id = "012345"
        user.created_at = user.updated_at = date
        userStr = user.__str__()
        self.assertIn("[User] (abcde)", userstr)
        self.assertIn("'id': '012345'", userstr)
        self.assertIn("'created_at': " + dateRepr, userStr)
        self.assertIn("'updated_at': " + dateRepr, userStr)

    def test_args_unused(self):
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
