from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ContactMech(models.Model):
    contact_mech_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="contact_mechanisms")
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.postal_code}"

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=30, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.product_name

class OrderHeader(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_contact_mech = models.ForeignKey(ContactMech, on_delete=models.CASCADE, related_name="shipping_orders")
    billing_contact_mech = models.ForeignKey(ContactMech, on_delete=models.CASCADE, related_name="billing_orders")

    def __str__(self):
        return f"Order {self.order_id} for {self.customer}"

class OrderItem(models.Model):
    order_item_seq_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OrderHeader, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Item {self.product} in Order {self.order}"
