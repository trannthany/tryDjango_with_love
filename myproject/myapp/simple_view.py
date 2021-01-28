from django.http import HttpResponse
# Create your views here.
def hello(request):
    text = """<h1>Welcome to my app! </h1>"""
    return HttpResponse(text)