from django.urls import path
from apps.order import views

urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_product_list, name='cart_product_list'),
    path('create/', views.create_order, name='create_order'),
]
