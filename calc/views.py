from django.shortcuts import render
from django.http import HttpResponse

import json



def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

# Create your views here.

def enco(request):

    word = request.POST.get('bianma')

    word = json.dumps(word)

    return HttpResponse(word)