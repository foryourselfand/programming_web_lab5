from django.urls import path

from . import views


app_name = 'dots'
urlpatterns = [
    path('create', views.create, name='create'),
    path('table', views.table, name='table'),
]
