from django.urls import path, include
from orders.views import OrderListView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order_list'),
]
