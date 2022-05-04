from rest_framework import serializers
from .models import *


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = ['id', 'name']


class PhylumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phylum
        fields = ['id', 'name']


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['id', 'name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name']


class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = ['id', 'name']


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id', 'name']


class ScientificNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificName
        fields = ['id', 'name']


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ['id', 'classification_for', 'kingdom', 'phylum',
                  'class_name', 'order', 'genus', 'family', 'scientific_name']


class ConservationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConservationStatus
        fields = ['id', 'status']


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ['id', 'facts_for', 'prey', 'distinct_feature', 'habitat',
                  'diet', 'average_litter_size', 'lifestyle', 'favourite_food', 'group', 'name_of_young', 'group_behavior']

class PhysicalCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalCharacteristics
        fields = ['id', 'characters_of', 'skin_type', 'top_speed', 'lifespan', 'weight', 'height']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'description', 'classification',
                  'conservation_status', 'facts', 'locations']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'animal']
