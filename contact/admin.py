from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'subject')
    # list_display_links = ('id', 'title')
    # list_per_page = 25
    pass


admin.site.register(Contact)
