# from django.shortcuts import render

# def hello(request):
#     return render(request, "myapp/template/hello.html", {})

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")