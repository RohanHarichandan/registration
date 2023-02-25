from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
   path('',views.Home,name='home'),
   path('login',views.login_user,name='login'),
   path('signup',views.signup_user,name='signup'),
   path('logout',views.logout_user,name='logout')
]
