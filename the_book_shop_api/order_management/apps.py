from django.apps import AppConfig


def connect_signal():
    pass


class OrderManagementConfig(AppConfig):
    name = 'the_book_shop_api.order_management'
    verbose_name = 'Order Management'

    def ready(self):
        connect_signal()
