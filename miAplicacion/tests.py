from django.test import TestCase, Client
from Usuarios.utilities.utility import *
from datetime import datetime as dt

# Create your tests here.
class testUtilities(TestCase):

    def test_day(self):
        hoy = dt.now()
        self.assertEqual(hoy.day, return_today())

    def test_month(self):
        month = dt.now()
        self.assertEqual(month.month, return_month())
    
    def test_year(self):
        year = dt.now()
        self.assertEqual(year.year, return_year())

