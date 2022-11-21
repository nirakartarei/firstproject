from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse("this is first function")
def propose(request):
    return HttpResponse("<marquee>I LOVE YOU </marquee>")
def nirakar(request):
    return HttpResponse('<marquee> UPSC <h1>INDIAN ARMY</h1>\n<h1>INDIAN NAVY</h1>\n<h1>INDIAN AIR FORCE</h1></marquee>')
