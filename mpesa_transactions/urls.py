"""
URL configuration for the 'mpesa_transactions' app.
"""

from django.urls import path
from . import views

app_name ='mpesa_transactions'

urlpatterns = [
    path('', views.index, name='index'),
    path('records/', views.records, name='records')
]
