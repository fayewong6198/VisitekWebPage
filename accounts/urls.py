from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .API import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Your URLs...
    path('api/auth/', jwt_views.TokenObtainPair.as_view(),
         name='token_obtain_pair'),
    path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/register/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
