
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('product',views.product,name="product"),
    path('product_details',views.product_details,name="product_details"),
    path('category',views.category,name="category"),
    path('cart',views.cart,name="cart"),
    path('account',views.account,name="account"),


]
