from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Define the home view
def home(request):
    return HttpResponse('<h1>Testing, Testing :)</h1>')

def about(request):
    return render(request, 'about.html')

def puppies_index(request):
    return render(request, 'puppies/index.html',{'cats': cats})

class Puppies:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Puppies('Balto', 'Huskie', 'foul little demon', 3),
    Puppies('Hoops', 'Golden Retriever', 'diluted tortoise shell', 1),
    Puppies('Alpha', 'American Bulldog', '3 legged cat', 4)
]