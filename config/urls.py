from django.conf import settings
from django.conf.urls import include, url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

urlpatterns = [
    # UserView management
    url(r'^api/users/', include('the_book_shop_api.users.urls')),
    url(r'^api/inventory/', include('the_book_shop_api.inventory.urls')),
    url(r'^api/order_mgmt/', include('the_book_shop_api.order_management.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="The Book Shop API",
        default_version='v1',
        description="",
    ),
    validators=['flex', 'ssv'],
    public=True,
)

if settings.DEBUG:
    urlpatterns = [
        url(r'^docs/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None),
            name='schema-json'),
        url(r'^docs/swagger/$', schema_view.with_ui('swagger', cache_timeout=None),
            name='schema-swagger-ui'),
        url(r'^docs/redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
    ] + urlpatterns
