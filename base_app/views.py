from itertools import product
from django.contrib import messages
from django.shortcuts import render,redirect
from product.models import Category,Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

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


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your username or password is invalid.')
            return redirect('user_login')

    context={}
    return render(request, 'login_page.html', context)



def user_logout(request):
    logout(request)
    return redirect('user_login')   


def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, "Your new and reset password is not matching")
            return redirect('home')
        else:
            messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'user_register.html', context)