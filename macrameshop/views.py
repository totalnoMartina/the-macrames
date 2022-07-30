from django.shortcuts import render


def index(request):
    """ A view to display homepage """
    return render(request, 'macrameshop/index.html')