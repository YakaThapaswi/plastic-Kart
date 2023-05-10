from django.contrib import admin
from home.models import Product,Variant
from contact.models import Contact
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Contact)
# Register your models here.
