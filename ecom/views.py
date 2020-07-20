from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category,SubCategory,Product


def index(request):
    title = 'Online Shopping India | Buy Mobile, Electronics, Fashion...'
    product_list = []
    products = Product.objects.all().values()
    for i in products:
        
        i.update({'discounted_price': i["product_price"]*(60/100)+i["product_price"]})
        product_list.append(i)
    return render(request, 'ecom/home.html', {'title': title, 'product_list': product_list})


def about(request):
    return render(request, 'ecom/about.html')


def cart(request):
    if request.session.get('session_status') == 'logged_in' and request.session.get('user_id') == 1:
        return render(request, 'ecom/cart.html')
    else:
        return redirect('authentication:login')


def category(request):
    return render(request, 'ecom/category.html')


def blog(request):
    return render(request, 'ecom/blog.html')


def blogdetail(request):
    return render(request, 'ecom/blogdetail.html')
