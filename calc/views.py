from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    res = int(a) + int(b)
    return HttpResponse(str(res))


def add2(request, a, b):
    res = int(a) + int(b)
    # print('a', a)
    # print('b', b)
    # print('request', request)
    return HttpResponse(str(res))
