from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path('shop/',views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('single/<slug:slug>/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
    path('succes/', views.succes, name='successfully'),
    path('review/', views.review, name='review'),
    path('category/<str:cats>' , views.product_category , name='category'),
    path('login/' , views.loginPage , name='login'),
    path('logout/', views.logoutUser , name='logout'),
    path('register/' , views.register , name = 'register'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:product_slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/count/', views.cart_count, name='cart_count'),

]