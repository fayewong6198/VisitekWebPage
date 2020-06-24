from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/blogs/', blog_list),
    path('api/blogs/<int:pk>/', blog_detail),

    path('api/users/', get_users),
    path('api/users/<int:pk>/', user_detail),
    path('api/auth/login/', login),

    path('api/contacts/', contact_list),
    path('api/contacts/<int:id>/', detail_contact),
]
