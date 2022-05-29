from rest_framework.generics import ListAPIView
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
