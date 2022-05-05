from rest_framework import serializers
from .models import *


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = '__all__'


class PhylumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phylum
        fields = '__all__'


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = '__all__'


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


class ScientificNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificName
        fields = '__all__'


class ClassificationSerializer(serializers.ModelSerializer):
    kingdom = KingdomSerializer()
    phylum = PhylumSerializer()
    class_name = ClassNameSerializer()
    order = OrderSerializer()
    genus = GenusSerializer()
    family = FamilySerializer()
    scientific_name = ScientificNameSerializer()
    class Meta:
        model = Classification
        fields = '__all__'



class ConservationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConservationStatus
        fields = '__all__'


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = '__all__'

class PhysicalCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalCharacteristics
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    classification = ClassificationSerializer()
    conservation_status = ConservationStatusSerializer()
    facts = FactSerializer()
    location = LocationSerializer(many=True)
    physical_characteristics = PhysicalCharacteristicsSerializer()

    class Meta:
        model = Animal
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
