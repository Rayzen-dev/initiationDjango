from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('test/<int:id_licence>',  views.test, name='indexTest')
]
