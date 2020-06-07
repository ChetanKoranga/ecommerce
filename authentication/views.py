from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            request.session['is_logged'] = True
            return redirect('ecom:index')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('authentication:login')
    # if request.session.has_key('is_logged'):
    #     return redirect(request, 'ecom:index')
    return render(request, 'authentication/login.html')


def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("authentication:login")


def register(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        passwd1 = request.POST["passwd1"]
        passwd2 = request.POST["passwd2"]
        email = request.POST["email"]

        user = User.objects.create_user(
            username=username, email=email, password=passwd1, first_name=first_name, last_name=last_name)
        user.save()
        print("User created...")
        return redirect("/")

    else:
        return render(request, "registration/register.html")
