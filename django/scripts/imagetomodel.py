from django.core.files import File
from api.models import Image, Animal
import os


def run():
    ### Animal Images
    path = os.path.join(os.getcwd(), "..", "AnimalData", "animalImages")
    animals = Animal.objects.all()

    for animal in animals:
        ipath = os.path.join(path, animal.name)
        print("Creating object for", animal)
        for img in os.listdir(ipath):
            i = Image.objects.create(animal=animal)
            i.image.save(img, File(open(os.path.join(ipath, img), "rb")))
            i.save()
    
    ## Loation Images
    path = os.path.join(os.getcwd(), "..", "AnimalData", "LocationImages")
    
    for animal in animals:
        name = f"{animal.name}-location-map.jpg"
        print("Saving location image for", animal)
        if os.path.exists(os.path.join(path, name)):
            animal.locationimage.save(name, File(open(os.path.join(path, name), "rb")))
            animal.save()