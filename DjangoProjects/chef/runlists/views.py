from django.shortcuts import render
import requests
import subprocess
from django.contrib.auth.decorators import login_required

def homepage(request):
  return render(request,'runlists/mainpage.html')

@login_required
def input_page(request):
  return render(request,'runlists/input_page.html')
