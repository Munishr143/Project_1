from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Sample(request):
    return HttpResponse('Hello World!!!')
def Abhi(request):
    return HttpResponse('<h1><marquee>Abhi is the Intelligent guy.</h1></marquee>')
def Yash(request):
    return HttpResponse('Yash is a Chocalate boy, he is innocent than abhi!!!')