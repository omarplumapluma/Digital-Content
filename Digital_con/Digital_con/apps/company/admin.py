from django.contrib import admin
from .models import Company, Contact


class ContactAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Contacto model"""
    list_display = ('name_contact', 'email', 'company')
    list_filter = ('company',)

admin.site.register(Company)  # Use the default options
admin.site.register(Contact, ContactAdmin)  # Use the customized options