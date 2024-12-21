from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.ContactMech)
admin.site.register(models.OrderHeader)
admin.site.register(models.OrderItem)
admin.site.register(models.Product)
