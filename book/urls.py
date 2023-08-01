from django.urls import path,include
from book import views
urlpatterns = [
    path('', views.book, name='book'),
    path('account', views.account, name='account'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('orders', views.orders, name='orders'),
    path('kartwallet', views.kartwallet, name='kartwallet'),
    path('personalinf', views.personalinf, name='personalinf'),
    path('addbook', views.addbook, name='addbook'),
    path('addressbook/<str:st>', views.addressbook, name='addressbook'),
    path('payments', views.payments, name='payments'),
    path("addaddress",views.addaddress,name="addaddress"),
    #path('changesell/<int:id>', views.changesell, name='sellwaste'),
    path('sellwaste', views.sellwaste, name='sellwaste'),
    path('services',views.services,name='services'),
    path('userservice/<int:id>',views.userservice,name='userservice')
]