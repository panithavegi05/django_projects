from django.shortcuts import render  # type: ignore
from django.http import HttpResponse  # type: ignore
from django.template import loader  # type: ignore
def home(request): 
    return HttpResponse("welcome to home page")  
def firstpage(request): 
    return HttpResponse("this is first page") 
def secondpage(request): 
    return HttpResponse("this is second page") 
