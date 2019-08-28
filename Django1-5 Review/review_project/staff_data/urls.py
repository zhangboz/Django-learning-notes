from django.conf.urls import url, include
from django.contrib import admin
from staff_data import views


urlpatterns = [
    url(r'staffpage',views.staffpage, name = "staffpage"),
    url(r'staffform',views.staffform, name = "staffform"),
    url(r'$', views.index, name = "index"),
]