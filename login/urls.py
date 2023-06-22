
from django.contrib import admin
from django.urls import path,include
from login import views
urlpatterns = [
    path('',views.login),
    path('reset',views.reset),
    path('signup',views.sign_up)
]
