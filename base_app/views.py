from itertools import product
from django.contrib import messages
from django.shortcuts import render,redirect
from product.models import Category,Product

# Create your views here.
def home(request):
    category=Category.objects.all()
    product=Product.objects.all()

    context={
        'category':category,
        'product':product
    }
    return render(request,'index.html',context)


def category_product(request,slug):
    if(Category.objects.filter(slug=slug, status=True)):
        product=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'product':product, 'category':category}
        return render(request,'category_products.html',context)
 


def product_details(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=True)):
        if(Product.objects.filter(slug=prod_slug, status=True)):
            product=Product.objects.filter(slug=prod_slug, status=True).first
            context={'product':product}

    return render(request,'product-details.html',context)


      