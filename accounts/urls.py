from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .API import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Your URLs...
    #     path('api-auth/', include('rest_framework.urls')),
    #     path('api/taken', jwt_views.TokenObtainPair.as_view(),
    #          name='token_obtain_pair'),
    #     path('api/refresh/', jwt_views.TokenRefreshView.as_view(),
    #          name='token_refresh'),
]
