from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. Welcome to poggle")

def populate_db(request):
    #todo: method to populate words database from ./static/dictionary.json
    #todo: method should only ever run once
    return
