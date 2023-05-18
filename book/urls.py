from django.urls import path,include
from book import views
urlpatterns = [
    path('', views.book, name='book'),
    path('account', views.account, name='account'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('orders', views.orders, name='orders'),
    path('kartwallet', views.kartwallet, name='kartwallet'),
    path('personalinf', views.personalinf, name='personalinf'),
    path('addressbook', views.addressbook, name='addressbook'),
    path('payments', views.payments, name='payments'),
]