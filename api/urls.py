from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('test',  views.IndexView.as_view(), name='indexTest')
]
