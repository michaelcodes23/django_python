from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Puppies_List


# Create your views here.

#Define the home view
def home(request):
    return HttpResponse('<h1>Testing, Testing :)</h1>')

def about(request):
    return render(request, 'about.html')

# {'puppies': puppies} is a way to reference the model
def puppies_index(request):
    return render(request, 'puppies/index.html',{'puppies': puppies})

def puppies_create(request):
    return render(request, 'puppies/create.html')

class PuppyCreate(CreateView):
    model = Puppies_List
    # fields = '__all__'
    #Alternate way of specfying what attributes we want to consider in the create view
    fields = ['name', 'breed','description','price','age']
    success_url = '/puppies/'

class PuppyUpdate(UpdateView):
    model = Puppies_List
    fields = ['name', 'breed', 'description','age']

class PuppyDelete(DeleteView):
    model = Puppies_List
    success_url = '/puppies/'

#Model for local database
class Puppies():
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

puppies = [
    Puppies('Balto', 'Huskie', 'Brave partner', 3),
    Puppies('Hoops', 'Golden Retriever', 'Blond fur', 1),
    Puppies('Alpha', 'American Bulldog', '3 legged dog', 4)
]

