from django.db import models
from django.contrib.auth.models import User

from the_book_shop_api.inventory.models import Book
from the_book_shop_api.users.models import Address


class Order(models.Model):
    CART = 'C'
    PROCESSING = 'P'
    SHIPPED = 'L'
    STATUSES = [
        (CART, 'Cart Created'),
        (PROCESSING, 'Processing Order'),
        (SHIPPED, 'Items Shipped'),
    ]
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES, default=CART)

    def __str__(self):
        return "{}".format(self.url)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.item.title)


class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}, {}".format(self.order.username, self.order, self.address)
