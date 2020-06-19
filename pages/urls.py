
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail'),
    path('blogs/', views.blogs, name='blogs'),
    path('services/', views.service, name='services'),
    path('service-details/', views.detail_service, name='detail_service'),
    path('service-detail-consult/', views.service_detail_consult,
         name='service_detail_consult'),
    path('service-detail-manage/', views.service_detail_manage,
         name='service_detail_manage'),
    path('service-detail-outsource/', views.service_detail_outsource,
         name='service_detail_outsource'),
    path('service-detail-repair/', views.service_detail_repair,
         name='service_detail_repair'),
    path('service-detail-security/', views.service_detail_security,
         name='service_detail_security'),
    path('search/', views.search, name='search'),
    path('blog_filter/', views.filter_category, name='filter_category')

]

handler404 = views.customHandler404
handler500 = views.customHandler500
