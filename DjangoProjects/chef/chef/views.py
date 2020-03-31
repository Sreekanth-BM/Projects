from django.shortcuts import render, redirect
import requests
import subprocess
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

def homepage(request):
  return render(request,'mainpage.html')


def login_page(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      if 'next' in request.POST:
        return redirect(request.POST.get('next'))
      else:
        return render(request, 'mainpage.html')
    else:
      return render(request, 'login_error.html')
  else:
    return render(request, 'loginpage.html')

def logout_page(request):
  if request.method == 'POST':
    user = request.user.get_username()
    if len(user) == 0:
      user = "No user logged in"
    else:
      user = "'"+user+"' logged out successfully"
    logout(request)
  return render(request,'mainpage.html',{'user':user})
