from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

def ks_homepage(request):
  return render(request,'knifestatus/mainpage.html')
