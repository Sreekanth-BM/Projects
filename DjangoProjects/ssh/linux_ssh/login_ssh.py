from django.shortcuts import render, redirect

def sshing(request):
  render(request, 'linux_ssh/input_page.html')
