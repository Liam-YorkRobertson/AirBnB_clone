#!/usr/bin/python3
"""defines unittests city"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """unittests testing City class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def twoCitysIdUnique(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, user2.id)

    def twocitysDifferentCreatTime(self):
        city1 = City()
        sleep(0.1)
        city2 = City()
        self.assertLess(city1.created_at, user2.created_at)

    def twoCitysDifferentUpdateTime(self):
        city1 = City()
        sleep(0.1)
        city2 = City()
        self.assertLess(city1.updated_at, user2.updated_at)

    def stringRepTest(self):
        date = datetime.today()
        dateRepr = repr(date)
        city = City()
        city.id = "012345"
        city.created_at = user.updated_at = date
        cityStr = user.__str__()
        self.assertIn("[City] (abcde)", citystr)
        self.assertIn("'id': '012345'", citystr)
        self.assertIn("'created_at': " + dateRepr, cityStr)
        self.assertIn("'updated_at': " + dateRepr, cityStr)

    def unusedArgsTest(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def kwargsInstalTest(self):
        date = datetime.today()
        date_iso = date.isoformat()
        city = City(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(us.id, "000000")
        self.assertEqual(us.created_at, date)
        self.assertEqual(us.updated_at, date)

    def noKwargsInstalTest(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
