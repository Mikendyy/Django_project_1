from django.contrib import admin
from customers.models import Customer
from django.contrib.admin import site


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'city', 'email','business')
    search_fields = ('name','city')

    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(Customer, CustomerAdmin)

