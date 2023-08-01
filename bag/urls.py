from django.urls import path,include
from bag import views
urlpatterns = [
    path('mybag', views.bag, name='bag'),
    
    path('addtobag/<int:id>', views.add_to_cart, name='addtobag'),
    path('whistlist/',views.whis,name='whistlist'),
    path('addtowhis/<int:id>', views.add_to_whis, name='addtowhis'),
    path('cartwhis/<int:id>', views.cart_whis, name='cartwhis'),
    path('whistlist/<int:id>',views.add_to_cart, name='addtocart'),
    path('removecartitem/<int:id>',views.remove_cart_item, name='removecartitem'),
    path('removewhisitem/<int:id>',views.remove_whis_item, name='removewhisitem'),
    path('placeorder',views.placeorder, name='placeorder')
]
