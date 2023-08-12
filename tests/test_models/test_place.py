#!/usr/bin/python3
""" test place class"""


import unittest
from models.place import Place


class test_place(unittest.TestCase):
    """ class test_review check Place class test cases """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test city_id """

        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):

        """ test user_id """

        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test name"""

        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test description """

        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test number_rooms """

        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test number_bathroom """

        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test max_guest """

        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test price_by_night """

        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test latitude"""

        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test longitude """

        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ test amenity_ids """

        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
