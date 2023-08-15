#!/usr/bin/python3
""" test City class"""


import unittest
from models.city import City
from datetime import datetime


class test_City(unittest.TestCase):
    """ class test_review check City class test cases """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))
