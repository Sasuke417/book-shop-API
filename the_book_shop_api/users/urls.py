from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserCreate, AddressList, AddressDetail

urlpatterns = [
    path('signup/', UserCreate.as_view(), name="user-create"),
    path('signin/', obtain_auth_token, name="account_login"),
    path('address/', AddressList.as_view(), name="address-list"),
    path('address/<int:id>/', AddressDetail.as_view(), name="address-detail")
]
