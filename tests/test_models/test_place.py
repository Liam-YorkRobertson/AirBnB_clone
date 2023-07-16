#!/usr/bin/python3
"""defines unittests place"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """unittests testing Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Place.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(Place.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(Place.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(Place.last_name))

    def twoPlacesIdUnique(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, user2.id)

    def twoplacesDifferentCreatTime(self):
        place1 = Place()
        sleep(0.1)
        place2 = Place()
        self.assertLess(place1.created_at, user2.created_at)

    def twoPlacesDifferentUpdateTime(self):
        place1 = Place()
        sleep(0.1)
        place2 = Place()
        self.assertLess(place1.updated_at, user2.updated_at)

    def stringRepTest(self):
        date = datetime.today()
        dateRepr = repr(date)
        place = Place()
        place.id = "012345"
        place.created_at = user.updated_at = date
        placeStr = user.__str__()
        self.assertIn("[Place] (abcde)", placestr)
        self.assertIn("'id': '012345'", placestr)
        self.assertIn("'created_at': " + dateRepr, placeStr)
        self.assertIn("'updated_at': " + dateRepr, placeStr)

    def unusedArgsTest(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def kwargsInstalTest(self):
        date = datetime.today()
        date_iso = date.isoformat()
        place = Place(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(us.id, "000000")
        self.assertEqual(us.created_at, date)
        self.assertEqual(us.updated_at, date)

    def noKwargsInstalTest(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
