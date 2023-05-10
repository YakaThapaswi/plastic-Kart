from django.urls import path,include
from contact import views
urlpatterns = [
    path('mywhistlist', views.contact, name='contact'),
]