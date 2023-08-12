#!/usr/bin/python3
""" test City class"""


import unittest
from models.city import City

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
        self.assertEqual(type(new.state_id),str)
