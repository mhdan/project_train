from django.contrib import admin
from .models import Customers


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'email', 'mobile_number']
    list_display = ['__str__', 'email', 'mobile_number', 'create_date']
    list_filter = ['create_date']

