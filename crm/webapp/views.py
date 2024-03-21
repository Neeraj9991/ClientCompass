from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from . models import Record

# - Home Page


def home(request):
    return render(request, 'webapp/index.html')

# - Register a user


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)


# - Login a user

def login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')  # Dashboard

    context = {'form': form}

    return render(request, 'webapp/login.html', context=context)

# - Dashboard
@login_required(login_url='login')
def dashboard(request):

    cust_records = Record.objects.all()

    user_name = None
    if request.user.is_authenticated:
        user_name = request.user.username

    context = {'records': cust_records,
               'user_name': user_name,
               }

    return render(request, 'webapp/dashboard.html', context=context)

# - User logout
def logout(request):

    auth.logout(request)

    return redirect('login')
