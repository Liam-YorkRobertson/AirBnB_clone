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

    def noArgsInstallTest(self):
        self.assertEqual(Place, type(Place()))

    def newInstanceStoreTest(self):
        self.assertIn(Place(), models.storage.all().values())

    def idStringTest(self):
        self.assertEqual(str, type(Place().id))

    def createdDatetimeTest(self):
        self.assertEqual(datetime, type(Place().created_at))

    def updatedDatetimeTest(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Place.user_id))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Place.name))

    def nameClassAttTest(self):
        place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(Place()))
        self.assertNotIn("name", am.__dict__)

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
