from django.contrib import admin

from .models import *


class KingdomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class PhylumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ClassNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class GenusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ScientificNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'classification_for')

class ConservationStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

class FactAdmin(admin.ModelAdmin):
    list_display = ('id', 'facts_for')

class PhysicalCharacteristicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'characters_of')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'image')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'classification', 'conservation_status', 'locations')

# Register your models here.
admin.site.register(Kingdom, KingdomAdmin)
admin.site.register(Phylum, PhylumAdmin)
admin.site.register(ClassName, ClassNameAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Genus, GenusAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(ScientificName, ScientificNameAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(ConservationStatus, ConservationStatusAdmin)
admin.site.register(Fact, FactAdmin)
admin.site.register(PhysicalCharacteristics, PhysicalCharacteristicsAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Animal, AnimalAdmin)