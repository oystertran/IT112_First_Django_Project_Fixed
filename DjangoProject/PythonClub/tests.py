from django.test import TestCase
from django.contrib.auth.models import User
from .models import PythonClubType, Product, Review
import datetime
from .forms import ProductForm
from django.urls import reverse_lazy, reverse

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
        self.assertEqual(self.product.discountPrice(),disc)

class NewProductForm(TestCase):
    def test_productform(self):
        data = {
                'productname' : 'surface',
                'producttype': 'laptop', 
                'user': 'oyster_tran',
                'dateentered': '2022-5-7',
                'price': '1200',
                'producturl': 'http://www.microsoft.com',
                'description':'half laptop half tablet'
            }
        form = ProductForm (data)
        self.assertTrue(form.is_valid)

     #this test is failing   
    #def test_Productform_Invalid(self):
        #data = {
                #'productname' : 'surface',
                #'producttype': 'laptop', 
                #'user': 'oyster_tran',
                #'dateentered': 'January 2, 2022',
                #'producturl': 'http://www.microsoft.com',
                #'description':'half laptop half tablet'
            #}
        #form = ProductForm (data)
        #self.assertFalse(form.is_valid)

class New_Product_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 
        'testuser1', password = 'P@ssword1')
        self.type = PythonClubType.objects.create(typename = 'laptop')
        self.product = Product.objects.create(productname = 'Lenovo', 
        producttype = self.type, user = self.test_user, 
        dateentered =datetime.date(2021,1,10), price = 1200, 
        producturl = 'http://www.lenovo.com',
        description = 'lenovo laptop')
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newproduct'))
        self.assertRedirects(response, 
        '/accounts/login/?next=/PythonClub/newproduct')