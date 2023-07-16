#!/usr/bin/python3
"""defines unittests state"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """unittests testing State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(State.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(State.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(State.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(State.last_name))

    def twoStatesIdUnique(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, user2.id)

    def twostatesDifferentCreatTime(self):
        state1 = State()
        sleep(0.1)
        state2 = State()
        self.assertLess(state1.created_at, user2.created_at)

    def twoStatesDifferentUpdateTime(self):
        state1 = State()
        sleep(0.1)
        state2 = State()
        self.assertLess(state1.updated_at, user2.updated_at)

    def stringRepTest(self):
        date = datetime.today()
        dateRepr = repr(date)
        state = State()
        state.id = "012345"
        state.created_at = user.updated_at = date
        stateStr = user.__str__()
        self.assertIn("[State] (abcde)", statestr)
        self.assertIn("'id': '012345'", statestr)
        self.assertIn("'created_at': " + dateRepr, stateStr)
        self.assertIn("'updated_at': " + dateRepr, stateStr)

    def unusedArgsTest(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def kwargsInstalTest(self):
        date = datetime.today()
        date_iso = date.isoformat()
        state = State(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(us.id, "000000")
        self.assertEqual(us.created_at, date)
        self.assertEqual(us.updated_at, date)

    def noKwargsInstalTest(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
