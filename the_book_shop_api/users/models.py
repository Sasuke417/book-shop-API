from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    full_name = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.IntegerField()
    street_address_1 = models.CharField(max_length=250)
    street_address_2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
