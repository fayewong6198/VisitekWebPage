from django.conf.urls import url, include
from rest_framework import routers
# from .API import UserViewSet, RegisterAPI
from .API import *

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # url(r'api/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    # url(r'api/auth/register/', RegisterAPI.as_view()),
    url(r'api/auth/register/', user_detail),
    url(r'api/users/', users),

]
