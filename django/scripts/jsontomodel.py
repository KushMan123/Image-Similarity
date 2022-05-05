from api.models import *
import json
import os
import re

def create_classification(classification):
    attrmap = [(Kingdom, "kingdom"), 
                (Phylum, "phylum"), 
                (ClassName, "class", "class_name"),
                (Order, "order"), 
                (Family, "family"), 
                (Genus, "genus"),
                (ScientificName, "scientific name", "scientific_name")
            ]
    pmap = {}
    for a in attrmap:
        c = a[0]
        n = a[1]
        if value:=classification.get(n):
            pmap[a[-1]] = c.objects.get_or_create(name=value)[0]
    
    return Classification.objects.create(
        **pmap
    )

def create_conservation_status(conservation):
    return ConservationStatus.objects.get_or_create(status=conservation or "Not Extinct")[0]

def create_fact(fact):
    return Fact.objects.create(
        prey=fact.get("prey") or fact.get("main prey"),
        distinct_feature=fact.get("distinct feature"),
        habitat=fact.get("habitat"),
        diet=fact.get("diet"),
        lifestyle=fact.get("lifestyle"),
        favourite_food=fact.get("favorite food"),
        average_litter_size=fact.get("average litter size"),
        group=fact.get("group"),
        name_of_young=fact.get("name of young"),
        group_behavior=fact.get("group behaviour")
    )

def create_phy_char(pc):
    return PhysicalCharacteristics.objects.create(
        color=" ".join(re.findall("[A-Z][^A-Z]*",pc.get("color") or " ")),
        skin_type=pc.get("skin type"),
        top_speed=pc.get("top speed"),
        lifespan=pc.get("lifespan"),
        weight=pc.get("weight"),
        height=pc.get("height")
    )

def create_locations(locations):
    ls = []
    for l in locations:
        ls.append(Location.objects.get_or_create(name=l)[0])
    return ls

def run():
    path = os.path.join(os.getcwd(), "..", "AnimalData")
    for animal in os.listdir(path):
        p = os.path.join(path, animal)
        if os.path.isdir(p):
            continue

        with open(p) as f:
            jf = json.load(f)
        

        ### Create Classification Object
        c = create_classification(jf.get("classification"))

        ### Create Conservation Status Object
        cs = create_conservation_status(jf.get("conservation-status"))

        ### Create Fact Object
        f = create_fact(jf.get("facts"))

        ### Create Physical Characteristic Object
        pc = create_phy_char(jf.get("physical characteristics"))

        ### Create Locations
        locations = create_locations(jf.get("locations"))

        ### Create Animal
        animal = Animal.objects.create(
            name=animal.split(".")[0],
            classification=c,
            conservation_status=cs,
            facts= f,
            physical_characteristics=pc
        )

        animal.save()
        animal.location.add(*locations)
        print(animal)

