from django.urls import path
from .views import home,category_product,product_details


urlpatterns = [
    path('',home,name='home'),
    path('product/<str:slug>',category_product,name='category_product'),
    path('product/<str:cate_slug>/<str:prod_slug>',product_details,name='product_details'),
]
