from django.shortcuts import render
from django.contrib.auth.models import User


def landing(request):
    context = {}
    return render(request, 'index.html', context)
