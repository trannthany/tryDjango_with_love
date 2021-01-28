from django.http import HttpResponse
# Create your views here.
def hello(request, number):
    text = "<h1>Welcome to my app number %s! </h1>"% number
    return HttpResponse(text)