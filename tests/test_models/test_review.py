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

    def noArgsInstallTest(self):
        self.assertEqual(Review, type(Review()))

    def newInstanceStoreTest(self):
        self.assertIn(Review(), models.storage.all().values())

    def idStringTest(self):
        self.assertEqual(str, type(Review().id))

    def createdDatetimeTest(self):
        self.assertEqual(datetime, type(Review().created_at))

    def updatedDatetimeTest(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(Review.text))

    def nameClassAttTest(self):
        review = Review()
        self.assertEqual(str, type(Review.name))
        self.assertIn("name", dir(Review()))
        self.assertNotIn("name", am.__dict__)

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
