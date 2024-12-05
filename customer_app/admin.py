from django.contrib import admin
from .models import Customer, Product

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display =('full_name', 'email', 'phone')
    list_filter = ('last_name', 'email', 'phone')
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name', 'price')    

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)