from django.urls import path
from the_book_shop_api.order_management import views


urlpatterns = [
    path('order/', views.OrderList.as_view(), name='order-list'),
    path('order/<int:order_id>/', views.OrderDetail.as_view(), name='order-detail'),
    path('orderitem/', views.OrderItemList.as_view(), name='orderitem-list'),
    path('orderitem/<int:pk>/', views.OrderItemDetail.as_view(), name='orderitem-detail'),
    path('shipment/', views.ShipmentList.as_view(), name='shipment-list'),
    path('shipment/<int:shipment_id>/', views.ShipmentDetail.as_view(), name='shipment-detail')
]