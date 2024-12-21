# serializers.py

from rest_framework import serializers
from .models import Customer, ContactMech, Product, OrderHeader, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'last_name']

class ContactMechSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMech
        fields = ['contact_mech_id', 'customer', 'street_address', 'city', 'state', 'postal_code', 'phone_number', 'email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'color', 'size']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['order_item_seq_id', 'product', 'quantity', 'status']

class OrderHeaderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    shipping_contact_mech = ContactMechSerializer()
    billing_contact_mech = ContactMechSerializer()
    order_items = OrderItemSerializer(many=True)  # Use order_items instead of items

    class Meta:
        model = OrderHeader
        fields = ['order_id', 'order_date', 'customer', 'shipping_contact_mech', 'billing_contact_mech', 'order_items']
