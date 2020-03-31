from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def homepage_view(request):
  return render(request,'linux_ssh/mainpage.html')
