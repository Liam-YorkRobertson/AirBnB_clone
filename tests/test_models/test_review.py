#!/usr/bin/python3
"""defines unittests review"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """unittests testing Review class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def twoReviewsIdUnique(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, user2.id)

    def tworeviewsDifferentCreatTime(self):
        review1 = Review()
        sleep(0.1)
        review2 = Review()
        self.assertLess(review1.created_at, user2.created_at)

    def twoReviewsDifferentUpdateTime(self):
        review1 = Review()
        sleep(0.1)
        review2 = Review()
        self.assertLess(review1.updated_at, user2.updated_at)

    def stringRepTest(self):
        date = datetime.today()
        dateRepr = repr(date)
        review = Review()
        review.id = "012345"
        review.created_at = user.updated_at = date
        reviewStr = user.__str__()
        self.assertIn("[Review] (abcde)", reviewstr)
        self.assertIn("'id': '012345'", reviewstr)
        self.assertIn("'created_at': " + dateRepr, reviewStr)
        self.assertIn("'updated_at': " + dateRepr, reviewStr)

    def unusedArgsTest(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def kwargsInstalTest(self):
        date = datetime.today()
        date_iso = date.isoformat()
        review = Review(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(us.id, "000000")
        self.assertEqual(us.created_at, date)
        self.assertEqual(us.updated_at, date)

    def noKwargsInstalTest(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
