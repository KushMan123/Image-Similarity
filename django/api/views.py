import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files import File
from django.conf import settings

from .serializers import *
from .models import *
from .utils import predict_similarity_scores, calculate_similarities

@api_view(['POST'])
def animal_image(request):
    image = request.data["file"]
    response, path = predict_similarity_scores(image)
    request.session["filepk"] = path
    return Response(response)

@api_view(['GET'])
def animal_info(request, animal):
    animalobj = Animal.objects.get(name=animal)
    animal = AnimalSerializer(animalobj)
    return Response(animal.data)

@api_view(['GET'])
def similar_animal(request, animal):
        positives = [p.image for p in Image.objects.filter(animal__name=animal)[:2]]
        imgpath = request.session["filepk"]
        with open("."+imgpath) as f:
            anchor = File(f)
        result = calculate_similarities(anchor, *positives)
        return Response(result)


# class KingdomView(viewsets.ModelViewSet):
#     queryset = Kingdom.objects.all()
#     serializer_class = KingdomSerializer

# class PhylumView(viewsets.ModelViewSet):
#     queryset = Phylum.objects.all()
#     serializer_class = PhylumSerializer

# class ClassNameView(viewsets.ModelViewSet):
#     queryset = ClassName.objects.all()
#     serializer_class = ClassNameSerializer

# class OrderView(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
    
# class GenusView(viewsets.ModelViewSet):
#     queryset = Genus.objects.all()
#     serializer_class = GenusSerializer

# class FamilyView(viewsets.ModelViewSet):
#     queryset = Family.objects.all()
#     serializer_class = FamilySerializer

# class ScientificNameView(viewsets.ModelViewSet):
#     queryset = ScientificName.objects.all()
#     serializer_class = ScientificNameSerializer

# class ClassificationView(viewsets.ModelViewSet):
#     queryset = Classification.objects.all()
#     serializer_class = ClassificationSerializer

# class ConservationStatusView(viewsets.ModelViewSet):
#     queryset = ConservationStatus.objects.all()
#     serializer_class = ConservationStatusSerializer

# class FactView(viewsets.ModelViewSet):
#     queryset = Fact.objects.all()
#     serializer_class = FactSerializer

# class PhysicalCharacteristicsView(viewsets.ModelViewSet):
#     queryset = PhysicalCharacteristics.objects.all()
#     serializer_class = PhysicalCharacteristicsSerializer

# class LocationView(viewsets.ModelViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer

# class AnimalView(viewsets.ModelViewSet):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer

# class ImageView(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer