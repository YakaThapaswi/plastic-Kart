
from django.urls import path,include
from members import views
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('signup', views.signup_user, name='signup'),
    path('logout', views.logout_user, name='logout'),
]