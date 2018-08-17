from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'index'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('documents', views.DocumentsView.as_view(), name='documents'),
    path('login', views.LoginView, name='login'),
    path('logout', views.LogoutView, name='logout'),
]
