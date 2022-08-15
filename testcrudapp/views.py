from django.shortcuts import render
from django.http import HttpResponse


def customer(request):
    return render(request, 'testcrudapp/dashboard.html')
