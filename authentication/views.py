from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user:
            auth.login(request,user)
            return redirect('/')
        
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    return render(request, 'authentication/index.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        passwd1 = request.POST["passwd1"]
        passwd2 = request.POST["passwd2"]
        email = request.POST["email"]

        user = User.objects.create_user(username=username,email=email,password=passwd1,first_name=first_name,last_name=last_name)
        user.save()
        print("User created...")
        return redirect("/")
        
    else:
        return render(request,"registration/register.html")