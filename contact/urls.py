from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import newContact
# from .API import contact_list, detail_contact

urlpatterns = [
    path('contact/new/', newContact, name='contacts'),
    # path('api/contacts/', contact_list),
    # path('api/contacts/<int:id>/', detail_contact),
]
