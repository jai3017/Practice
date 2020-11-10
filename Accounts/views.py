from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):

    if request.method =='POST':
        #get form values
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        messages.error(request,'testing error message')
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'user already available')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'the email is being used')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                    # auth.login(request,user)
                    # messages.success(request,'you are now logged-in')
                    # return redirect(request,'index.html')
                    user.save()
                    messages.success(request,'you are now registeres and you are eligible to logged-in')
                    return redirect('login')



        else:
            messages.error(request,'passwords do not match')
        return redirect('register')
        # register
    else:
        return render(request,'Accounts/register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in ')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username and password')
            return redirect('login')
        # register
    else:
        return render(request, 'Accounts/login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'you are now logged out')
        return redirect('index.html')


def dashboard(request):
    return render(request, 'Accounts/dashboard.html')
