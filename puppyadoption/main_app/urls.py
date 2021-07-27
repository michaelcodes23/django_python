from django.urls import path
from . import views
from .views import PuppyCreate, PuppyUpdate, PuppyDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('puppies/', views.puppies_index, name='puppies'),
    # path('puppies/<int:puppy_id>/', views.cats_detail, name = 'detail'),
    # New route used to show a form and create a new cat
    path('puppies/create/', views.PuppyCreate.as_view(), name = 'puppies_create'),
    #Update Route
    path('puppies/<int:pk>/update/', views.PuppyUpdate.as_view(), name = 'puppies_update'),
    path('puppies/<int:pk>/delete/', views.PuppyDelete.as_view(), name = 'puppies_delete'),
]