# views.py

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Customer, ContactMech, Product, OrderHeader, OrderItem
from .serilizers import CustomerSerializer, ContactMechSerializer, ProductSerializer, OrderHeaderSerializer, OrderItemSerializer


# Order API Viewset
class OrderHeaderViewSet(viewsets.ModelViewSet):
    queryset = OrderHeader.objects.all()
    serializer_class = OrderHeaderSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def create(self, request, *args, **kwargs):
        # Handle POST request to create an order
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # Handle GET request to retrieve an order by ID
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Handle PUT request to update an order
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Handle DELETE request to delete an order
        return super().destroy(request, *args, **kwargs)

# Order Item API Viewset
# Order Item API Viewset
class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return OrderItem.objects.filter(order_id=order_id)

    def perform_create(self, serializer):
        order_id = self.kwargs['order_id']
        order = OrderHeader.objects.get(id=order_id)
        serializer.save(order=order)

    def create(self, request, *args, **kwargs):
        # Handle POST request to add an item to an order
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Handle PUT request to update order item quantity or status
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Handle DELETE request to remove an item from an order
        return super().destroy(request, *args, **kwargs)
