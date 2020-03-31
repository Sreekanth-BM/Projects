from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cv_homepage_view(request):
  return render(request,'chefversion/mainpage.html')
