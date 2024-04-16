from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User #BD component
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def register(request):
    #print(request.META) - Get request data.
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm =request.POST.get('password_confirm')
        #return HttpResponse(f'{username}-{email}-{password}') Get the inputs.
        if password != password_confirm:
            messages.add_message(request, constants.ERROR, "The passwords did not MATCH! ")
            return redirect('/users/register')
        if len(password)<6:
            messages.add_message(request, constants.ERROR, "The password must have more than 6 digits. ")
            return redirect('/users/register')
        #users = User.objects.all() Returns all the objs from BD
        users = User.objects.filter(username=username) # Returns only if this username already exists in the DB.
        print(users)
        if users.exists():
            messages.add_message(request, constants.ERROR, "User already exists in the DB!")
            return redirect('/users/register')
        # Saving user in the DB: 
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("/users/login/")
        #return HttpResponse(f' User successfully created: {username}-{email}-{password}')
        
def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # Searching for user in the DB: 
        userExists = auth.authenticate(request, username=username, password=password)
        
        if(userExists):
            auth.login(request, userExists)
            return redirect("patients/home")
        messages.add_message(request, constants.ERROR, "Incorrect username or password.")
        return redirect("users/login/")

def logout(request):
    #print(request.user.is_authenticated) is there a logged user?
    auth.logout(request)
    return redirect("users/login")