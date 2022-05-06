from django.test import TestCase
from django.contrib.auth.models import User
from .models import PythonClubType, Product, Review
import datetime

# Create your tests here.

class PythonClubTypeTest(TestCase):
    def setUp(self):
        self.type=PythonClubType(typename='Lenovo Laptop')
        
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Lenovo Laptop')

    def test_tablename(self):
        self.assertEqual(str(PythonClubType._meta.db_table), 
        'PythonClubType')

class ProductTest(TestCase):
    def setUp(self):
        self.type = PythonClubType(typename='Laptop')
        self.User = User(username = 'user1')
        self.product = Product(productname = 'Lenovo', 
        producttype = self.type, user = self.User, 
        dateentered =datetime.date(2021,1,10), price = 1200, 
        producturl = 'http://www.lenovo.com',
        description = 'lenovo laptop')

    def test_string(self):
        self.assertEqual(str(self.product),'Lenovo')
    
    def test_discount(self):
        disc = self.product.price * .05
        self.assertEqual(self.product.discountAmount(),disc)

    def test_discountedAmount(self):
        disc = self.product.price*(1- .05)
        self.assertEqual(self.product.discountPrice(),1,140.94)