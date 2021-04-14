import factory
from factory import fuzzy
from the_book_shop_api.users.models import Address


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username', )
    username = factory.Sequence(lambda n: 'user-{}'.format(n))
    email = factory.Sequence(lambda n: 'user-{}@example.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address
    user = factory.SubFactory(UserFactory)
    full_name = fuzzy.FuzzyText()
    mobile_number = fuzzy.FuzzyInteger(low=7000000000)
    # street_address_1 = models.CharField(max_length=250)
    # street_address_2 = models.CharField(max_length=250, blank=True)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    pincode = fuzzy.FuzzyInteger(low=100000)
    # country = models.CharField(max_length=50)

