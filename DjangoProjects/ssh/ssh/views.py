from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
import requests

def homepage_view(request):
  return render(request,'mainpage.html')


def login_view(request):
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
    return render(request, 'loginpage.html')  

def logout_view(request):
  if request.method == 'POST':
    user = request.user.get_username()
    if len(user) == 0:
      user = "No user logged in"
    else:
      user = "'"+user+"' logged out successfully"
    logout(request)
  return render(request,'mainpage.html',{'user':user})
