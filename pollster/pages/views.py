from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
def signup(request):
    return render(request, 'pages/signup.html')
def creator(request):
    return render(request, 'pages/creator.html')