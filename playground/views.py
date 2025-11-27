from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Haadi'})
