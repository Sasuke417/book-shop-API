from test_plus.test import TestCase
from django.contrib.auth.models import User
from the_book_shop_api.users.models import Address


class TestModel(TestCase):
    """test to check if all the required fields are declared in each model"""

    def test_create_address(self):
        user = User.objects.create_user(username='test_user', email='test.user@tcs.com',
                                        password='its secret :-)')
        full_name = "test user"
        mobile_number = 123456789
        street_address_1 = "10 downing street"
        street_address_2 = ""
        city = "Westminster"
        state = "London"
        pincode = 123456
        country = "United Kingdom"
        addr1 = Address.objects.create(user=user, full_name=full_name, mobile_number=mobile_number,
                                       street_address_1=street_address_1,
                                       street_address_2=street_address_2, city=city, state=state,
                                       pincode=pincode, country=country)
        self.assertIsNotNone(addr1)
        addr2 = Address.objects.create(user=user, full_name=full_name, mobile_number=mobile_number,
                                       street_address_1=street_address_1, city=city, state=state,
                                       pincode=pincode, country=country)
        self.assertIsNotNone(addr2)
        self.assertEquals(len(user.address.all()), 2)
