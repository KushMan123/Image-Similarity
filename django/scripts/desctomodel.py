import json
import os
from api.models import Animal

def run():
    path = os.path.join(os.getcwd(), "..", "AnimalData", "description.json")
    with open(path) as f:
        d = json.load(f)

    for name, desc in d.items():
        a = Animal.objects.get(name=name)
        a.description = desc
        a.save()