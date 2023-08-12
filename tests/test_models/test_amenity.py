#!/usr/bin/python3
""" test Amenity class"""


import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ class test_review check Amenity class test cases """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
