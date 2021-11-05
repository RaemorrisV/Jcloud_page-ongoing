from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'indexapp/index.html')

def user_guide(request):
    return render(request,'indexapp/user-guide.html')

def feature(request):
    return render(request,'indexapp/feature.html')

def jdevops(request):
    return render(request,'indexapp/jdevops.html')