# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderHeaderViewSet, OrderItemViewSet

# Router to automatically handle routes
router = DefaultRouter()
router.register(r'', OrderHeaderViewSet)
router.register(r'(?P<order_id>\d+)/items', OrderItemViewSet, basename='orderitem')

urlpatterns = [
    path('', include(router.urls)),
]
