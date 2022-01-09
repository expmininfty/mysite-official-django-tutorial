from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, you're a the polls index.")