from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('signup',views.signup,name="SignUp"),
    path('regsignup',views.signupHandle,name="signHandle"),
    path('login',views.loginhandle,name="LogInHandle"),
    path('logout',views.logoutHandle,name="LogInHandle"),
    path('about',views.about,name="about"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('menuitem',views.menu,name="menu_item")
]
