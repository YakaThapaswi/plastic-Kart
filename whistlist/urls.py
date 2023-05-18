from django.urls import path,include
from whistlist import views
urlpatterns = [
    path('', views.whistlist, name='whistlist'),
    path('cart',views.cart,name='cart'),
]