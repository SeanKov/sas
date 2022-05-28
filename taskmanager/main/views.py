from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def math(request):
    return render(request, 'main/math.html')


def hebrew(request):
    return render(request, 'main/hebrew.html')


def ezrahut(request):
    return render(request, 'main/ezrahut.html')


def history(request):
    return render(request, 'main/history.html')


def english(request):
    return render(request, 'main/english.html')


def art(request):
    return render(request, 'main/art.html')


def russian(request):
    return render(request, 'main/russian.html')




