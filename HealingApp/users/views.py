from django.shortcuts import render, redirect
from django.contrib.auth.models import User #BD component
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login

def register(request):
    #print(request.META) - Get request data.
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm =request.POST.get('password_confirm')
        #return HttpResponse(f'{username}-{email}-{password}') #Get the inputs.
        if password != password_confirm:
            messages.add_message(request, constants.ERROR, 'The passwords did not MATCH! ')
            return redirect("/users/register")
        if len(password)<6:
            messages.add_message(request, constants.ERROR, 'The password must have at least, 6 digits. ')
            return redirect("/users/register") 
        #users = User.objects.all() #Returns all the objs from BD
        users = User.objects.filter(username=username) # Returns only if this username already exists in the DB.
        print(users)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'User already exists in the DB!')
            return redirect("./users/register")
        else:
            try:
                User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
                messages.add_message(request, constants.SUCCESS, "User successfully registered. Just log in.")
                return redirect("/users/login")
            except:
                messages.add_message(request, constants.ERROR, 'Error on trying to register the user.')
                return redirect("/users/register")
                #return HttpResponse(f' User successfully created: {username}-{email}-{password}')
            
def login_view(request):
    if request.method=="GET":
        return render(request, 'login.html')
    elif request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = User.objects.get(username=username)
        authenticate(request, username=username)
        pwd = user.check_password(password)

        #print('User Exists ', user) OK

        if user is not None and pwd:
            login(request, user)
            return redirect('/patients/home')
            #return render(request, '/patients/home')
        else: 
            messages.add_message(request, constants.ERROR, 
                             'An authentication error ocurred. Check user and password.')
            return redirect('/users/login/')

def logout(request):
    #print(request.user.is_authenticated) is there a logged user?
    auth.logout(request)
    return redirect('/users/login')