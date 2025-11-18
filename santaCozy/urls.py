from django.urls import path
from .views import *

app_name = 'santaCozy'

urlpatterns = [
    path('', index, name='index'),
    path('loading/', loading, name='loading'),
    path('result/', result, name='result'),
]