from django.conf.urls import url
from django.contrib import admin
from AppTwo import views
from django.conf.urls import include
urlpatterns = [
    # url(r'^$', views.Help, name='Help'),
    url(r'^$', views.Help, name='Help'),
]