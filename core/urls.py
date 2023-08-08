from django.urls import path
from core.views import *

urlpatterns = [
    path('about',about),
    path('contact',contact),
    path('',index),
    path('login',login),
    path('signup',signup),
    path('shop',shop),
    path('vegetables',vegetables),
 
]
