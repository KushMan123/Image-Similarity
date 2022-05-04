from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets 
from .serializers import *
from .models import *


# def index(request):
#     return HttpResponse("Hello. You're at the api index.")

class KingdomView(viewsets.ModelViewSet):
    queryset = Kingdom.objects.all()
    serializer_class = KingdomSerializer

class PhylumView(viewsets.ModelViewSet):
    queryset = Phylum.objects.all()
    serializer_class = PhylumSerializer

class ClassNameView(viewsets.ModelViewSet):
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class GenusView(viewsets.ModelViewSet):
    queryset = Genus.objects.all()
    serializer_class = GenusSerializer

class FamilyView(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class ScientificNameView(viewsets.ModelViewSet):
    queryset = ScientificName.objects.all()
    serializer_class = ScientificNameSerializer

class ClassificationView(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer

class ConservationStatusView(viewsets.ModelViewSet):
    queryset = ConservationStatus.objects.all()
    serializer_class = ConservationStatusSerializer

class FactView(viewsets.ModelViewSet):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer

class PhysicalCharacteristicsView(viewsets.ModelViewSet):
    queryset = PhysicalCharacteristics.objects.all()
    serializer_class = PhysicalCharacteristicsSerializer

class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AnimalView(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer