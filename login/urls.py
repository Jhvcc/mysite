# -*- coding: utf-8 -*-
__author__ = '胡弦'
__date__ = '2020/5/19 0019 下午 16:31'

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
]