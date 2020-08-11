from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('myproduct',views.myproduct,name='myproduct'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('myproductsearch',views.myproductsearch,name='myproductsearch'),
    path('search',views.search,name='search'),
    path('delete/<post_id>',views.delete_post,name='delete')

]
