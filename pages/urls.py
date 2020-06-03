
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog1/<int:id>', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('services/', views.service, name='service'),
    path('service-details/', views.detail_service, name='detail_service'),
    path('service-consult/', views.service_detail_consult,
         name='service_detail_consult'),
    path('service-detail-manage/', views.service_detail_manage,
         name='service_detail_manage'),
    path('service-detail-outsource/', views.service_detail_outsource,
         name='service_detail_outsource'),
    path('service-detail-repair/', views.service_detail_repair,
         name='service_detail_repair'),
    path('service-detail-security/', views.service_detail_security,
         name='service_detail_security'),

]
