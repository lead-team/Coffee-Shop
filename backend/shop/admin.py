from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(UserOrder)
admin.site.register(Storage)



