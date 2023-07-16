#!/usr/bin/python3
"""defines unittests amenity"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """unittests testing Amenity class."""

    def noArgsInstallTest(self):
        self.assertEqual(Amenity, type(Amenity()))

    def newInstanceStoreTest(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def idStringTest(self):
        self.assertEqual(str, type(Amenity().id))

    def createdDatetimeTest(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def updatedDatetimeTest(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def nameClassAttTest(self):
        amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def twoAmenitysIdUnique(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, user2.id)

    def twoamenitysDifferentCreatTime(self):
        amenity1 = Amenity()
        sleep(0.1)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, user2.created_at)

    def twoAmenitysDifferentUpdateTime(self):
        amenity1 = Amenity()
        sleep(0.1)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, user2.updated_at)

    def stringRepTest(self):
        date = datetime.today()
        dateRepr = repr(date)
        amenity = Amenity()
        amenity.id = "012345"
        amenity.created_at = user.updated_at = date
        amenityStr = user.__str__()
        self.assertIn("[Amenity] (abcde)", amenitystr)
        self.assertIn("'id': '012345'", amenitystr)
        self.assertIn("'created_at': " + dateRepr, amenityStr)
        self.assertIn("'updated_at': " + dateRepr, amenityStr)

    def unusedArgsTest(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def kwargsInstalTest(self):
        date = datetime.today()
        date_iso = date.isoformat()
        amenity = Amenity(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(us.id, "000000")
        self.assertEqual(us.created_at, date)
        self.assertEqual(us.updated_at, date)

    def noKwargsInstalTest(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
