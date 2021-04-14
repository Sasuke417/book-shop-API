from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'the_book_shop_api.users'
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            import the_book_shop_api.users.signals  # noqa F401
        except ImportError:
            pass
