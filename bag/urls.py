from django.urls import path,include
from bag import views
urlpatterns = [
    path('mybag', views.bag, name='bag'),
]