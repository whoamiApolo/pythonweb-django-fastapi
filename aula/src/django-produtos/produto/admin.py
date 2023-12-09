from django.contrib import admin

# Register your models here.
from produto.models import Product

admin.site.register(Product)