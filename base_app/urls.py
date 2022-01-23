from django.urls import path
from .views import home,category_product,product_details,user_login,user_logout,user_register


urlpatterns = [
    path('home/',home,name='home'),
    path('product/<str:slug>',category_product,name='category_product'),
    path('product/<str:cate_slug>/<str:prod_slug>',product_details,name='product_details'),
    path('', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/',user_register,name='user_register')
]
