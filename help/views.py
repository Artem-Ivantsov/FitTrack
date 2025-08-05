from django.shortcuts import render
from django.http import HttpResponse


def help(request):
    return render(request,("help/help.html"))


def report(request):
    return render(request,("help/exports.html"))

def privacy_policy(request):
    return render(request,("help/privacy_policy.html"))

def privacy_policy_full(request):
    return render(request,("help/privacy_policy_full.html"))