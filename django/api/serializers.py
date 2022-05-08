from rest_framework import serializers
from .models import *


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        exclude = ("id", )

class PhylumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phylum
        exclude = ("id", )

class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        exclude = ("id", )

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ("id", )

class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        exclude = ("id", )

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        exclude = ("id", )

class ScientificNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificName
        exclude = ("id", )

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
        exclude = ("id", )

class ConservationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConservationStatus
        exclude = ("id", )

class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        exclude = ("id", )

class PhysicalCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalCharacteristics
        exclude = ("id", )

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ("id", )


class AnimalSerializer(serializers.ModelSerializer):
    classification = ClassificationSerializer()
    conservation_status = ConservationStatusSerializer()
    facts = FactSerializer()
    location = LocationSerializer(many=True)
    physical_characteristics = PhysicalCharacteristicsSerializer()

    class Meta:
        model = Animal
        exclude = ("id", )

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ("id", )
