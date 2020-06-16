from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    title = 'Online Shopping India | Buy Mobile, Electronics, Fashion...'
    return render(request, 'ecom/home.html', {'title': title})


def about(request):
    if request.session.has_key('is_logged'):
        return render(request, 'ecom/about.html')
    else:
        messages.info(request, 'Session not logged in')
        return render(request, 'ecom/about.html')


def cart(request):
    if request.session.has_key('is_logged'):
        return render(request, 'ecom/cart.html')
    else:
        return redirect('authentication:login')


def category(request):
    return render(request, 'ecom/category.html')


def blog(request):
    return render(request, 'ecom/blog.html')


def blogdetail(request):
    return render(request, 'ecom/blogdetail.html')
