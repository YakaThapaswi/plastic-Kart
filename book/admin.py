from django.contrib import admin
from book.models import Address,Order,Sell
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Sell)
