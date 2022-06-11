import unittest
from django.test import TestCase


class Check(unittest.TestCase):
    def check_test():
        x = 12
        assert(x+x == 24)

