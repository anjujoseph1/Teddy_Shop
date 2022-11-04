from django.urls import path
from . import views
urlpatterns = [
    #cart
    path('cartDetails/', views.cartdetails, name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min/<int:product_id>/', views.min_cart, name='mincart'),
    path('remove/<int:product_id>/', views.remove, name='remove'),
    
    #home
    path('',views.home,name='frontpage'),
    path('<slug:c_slug>/',views.home,name='frontpage'),
    path('shop',views.shop,name='shop'),
    path('<slug:c_slug>/<slug:product_slug>',views.view,name='view'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('service',views.service,name='service'),

    #Register
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
]
