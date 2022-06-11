import unittest
from django.test import TestCase


class Check_test(unittest.TestCase):

    def test_check(self):
        x = 12
        assert(x+x == 24)

