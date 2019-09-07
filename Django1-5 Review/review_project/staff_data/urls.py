from django.conf.urls import url, include
from django.contrib import admin
from staff_data import views
from django.contrib.auth.views import login

app_name = "staff_data"
urlpatterns = [
    url(r'staffpage',views.staffpage, name = "staffpage"),
    url(r'staffform',views.staffform, name = "staffform"),
    url(r'$', views.index, name = "index"),
    url(r'^staff_login/$', views.staff_login, name = "staff_login_name")
]