from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'Home/Home.html')

def login(request):
    return render(request, 'Home/Login.html')

def signup(request):
    return render(request, 'Home/Signup.html')

def analysis(request):
    return render(request, 'Home/Analysis.html')

# def profile(request):
#     return render(request, 'Home/Profile.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full-name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new UserProfile object with the form data
        user_profile = UserProfile(username=username, full_name=full_name, dob=dob, email=email, password=password)
        user_profile.save()

        # Redirect the user to a success page
        return redirect('home')
    else:
        return render(request, 'Home/Signup.html')
    


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)  # Set session to expire in 2 weeks
            else:
                request.session.set_expiry(0)  # Set session to expire when browser closes
            return redirect('home')
        else:
            # Check if user exists in UserProfile model
            try:
                user_profile = UserProfile.objects.get(username=username)
            except UserProfile.DoesNotExist:
                user_profile = None

            if user_profile is not None and user_profile.check_password(password):
                # Create user object and login user
                user = user_profile.user
                login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # Set session to expire in 2 weeks
                else:
                    request.session.set_expiry(0)  # Set session to expire when browser closes
                return redirect('home')
            else:
                # Authentication failed
                error_message = 'Invalid username or password.'
                return render(request,  'Home/Home.html', {'error_message': error_message})

    return render(request,  'Home/Home.html')