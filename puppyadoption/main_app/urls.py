from django.urls import path
from . import views
from .views import Puppies

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('puppies/', views.puppies_index, name='puppies'),
    # path('puppies/<int:puppy_id>/', views.cats_detail, name = 'detail'),
    # New route used to show a form and create a new cat
    path('puppies/create/', views.puppies_create, name = 'puppies_create')
]