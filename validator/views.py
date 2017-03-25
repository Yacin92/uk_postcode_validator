from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import validation


def index(request):

    return render (request, 'validator/index.html')


def validate(request):

    if(request.method == "POST"):
        code = request.POST["postcode"]
        if validation.is_valid(code):
            code_status = 'valid'
        else:
            code_status ='invalid'
        return render (request, 'validator/result.html', {'code_status':code_status})
