# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
import requests
from django.contrib.auth.decorators import login_required


# on requesting 'wssh_homepage' url.
@login_required()
def homepage_view(request):
  return render(request,'windows_winrm/mainpage.html')
