# wallets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_wallet/', views.create_wallet, name='create_wallet'),
    path('add_coins/', views.add_coins, name='add_coins'),
    path('get_balance/<str:student_name>/', views.get_balance, name='get_balance'),
]

