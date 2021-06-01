from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import User


def home(request):
    users = User.objects.all()
    return render(request,"index.html",context={"Title":"shy",'name':"中国人","users":users})