from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return JsonResponse({"data":"zph"})
