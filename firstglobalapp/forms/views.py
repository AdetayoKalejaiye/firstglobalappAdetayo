from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import SignUp, SignIn
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.utils import translation
# Create your views here.

def signUp(request):
    if request.method == 'GET':
        try:
            return render(request, 'signUp.html', {'form':SignUp} )
        except IntegrityError:
            return render(request,'signUp.html', {'form':SignUp, 'error':'Username already taken. Choose new username.'})
 
    else:
        if request.POST['password1'] ==request.POST['password2']:
            user = User.objects.create_user( request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signUp.html', {'form':SignUp, 'error':'Passwords do not match'})
    

def signIn(request):
    if request.method == 'POST':
        form = SignIn(request, request.POST)
        if form.is_valid():
            if form.cleaned_data.get('remember_me'):
                # If "Remember Me" is checked, set the session duration to a longer period
                request.session.set_expiry(1209600)  # 2 weeks (in seconds)
            else:
                # If "Remember Me" is not checked, use the default session behavior
                request.session.set_expiry(0)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = SignIn()

    return render(request, 'signIn.html', {'form': form})

def home(request):
    return render(request, 'index.html')

def test(request):
    if request.method == 'GET':
        return render(request, 'test.html', {'form':SignIn})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password']) 
    if user is None:
        return render(request,'test.html', {'form': SignIn,  'error': 'username and password do not match'})
    else: 
        login(request,user)
        return redirect('home')





# def loginaccount(request): 
#     if request.method == 'GET':
#         return render(request, 'loginaccount.html', {'form':AuthenticationForm})
#     else:
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password']) 
#     if user is None:
#         return render(request,'loginaccount.html', {'form': AuthenticationForm(),  'error': 'username and password do not match'})
#     else: 
#         login(request,user)
#         return redirect('home')