from django.urls import path

from .views import animal_image, animal_info, similar_animal

urlpatterns = [
    path('animalimage/', animal_image, name='Animal Image'),
    path('animal/<str:animal>/', animal_info, name='Animal Information'),
    path('similarimage/<str:animal>/', similar_animal, name='Similar Image')
]