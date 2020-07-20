from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout


def login(request):
    if not request.session.get('session_status') == 'logged_in' and not request.session.get('user_id') == 1:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                request.session['user_id'] = 1
                request.session['session_status'] = 'logged_in'
                return redirect('ecom:index')

            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('authentication:login')
            # if request.session.has_key('is_logged'):
            #     return redirect(request, 'ecom:index')
        else:
            return render(request, 'authentication/login.html')
    else:
        return redirect('ecom:index')


def signout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("authentication:login")


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        passwd1 = request.POST["password"]
        passwd2 = request.POST["confirm_password"]
        email = request.POST["email"]
        if passwd1 == passwd2:
            user = User.objects.create_user(
                username=username, email=email, password=passwd1, first_name=first_name, last_name=last_name)
            user.save()
            print("User created...")
            return redirect("authentication:login")
        else:
            messages.error(
                request, "Passwords doesn't matched.")
            return render(request, "authentication/register.html")

    else:
        return render(request, "authentication/register.html")


def setCookie():
    if not request.COOKIES.get('team'):
        response = HttpResponse("Visiting for the first time.")
        response.set_cookie('team', 'barcelona', max_age=1200)
        return response
    else:
        return HttpResponse("Your favorite team is {}".format(request.COOKIES['team']))


def save_session_data(request):
    # set new data
    request.session['user_id'] = 20
    request.session['team'] = 'Barcelona'
    return HttpResponse("Session Data Saved")


def access_session_data(request):
    response = ""
    if request.session.get('user_id'):
        user_id = request.session.get('user_id')
        response += "User Id : {0} <br>".format(user_id)
    if request.session.get('team'):
        team = request.session.get('team')
        response += "Team : {0} <br>".format(team)

    if not response:
        return HttpResponse("No session data")
    else:
        return HttpResponse(response)


def delete_session_data(request):
    try:
        del request.session['user_id']
        del request.session['team']
    except KeyError:
        pass

    return HttpResponse("Session Data cleared")
