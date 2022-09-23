from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. At the polls index.")
