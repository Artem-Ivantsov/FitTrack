from django.shortcuts import render
from django.http import HttpResponse


def help(request):
    return render(request,("help/help.html"))


def report(request):
    return render(request,("help/exports.html"))