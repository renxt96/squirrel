from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi! Welcome to the Squirrel Tracker.")
