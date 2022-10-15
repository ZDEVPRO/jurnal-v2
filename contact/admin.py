from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'create_time', 'create_date']
    readonly_fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'ip', 'create_time', 'create_date']


admin.site.register(Contact, ContactAdmin)
