import unittest
from django.test import TestCase

class Test_SB_APIs(unittest.TestCase):

    def test_name(self):
        name = 'Muzammil'
        self.assertEqual(name, 'Muzammil')
        
    def test_pass(self):
        password = 'abc123'
        self.assertEqual(password, 'abc')