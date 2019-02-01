from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def page_not_found(request):
    print(request)
    return HttpResponse('genki/hello.html')


