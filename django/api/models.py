from django.db import models

class Kingdom(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Phylum(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class ClassName(models.Model):
    class Meta:
        verbose_name = 'Class Name'

    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Genus(models.Model):
    class Meta:
        verbose_name_plural = 'Genuses'

    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Family(models.Model):
    class Meta:
        verbose_name_plural = 'Families'
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class ScientificName(models.Model):
    class Meta:
        verbose_name = 'Scientific Name'
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Classification(models.Model):
    kingdom = models.ForeignKey(Kingdom, on_delete=models.DO_NOTHING, null=True, blank=True)
    phylum = models.ForeignKey(Phylum, on_delete=models.DO_NOTHING, null=True, blank=True)
    class_name = models.ForeignKey(ClassName, on_delete=models.DO_NOTHING, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=True, blank=True)
    genus = models.ForeignKey(Genus, on_delete=models.DO_NOTHING, null=True, blank=True)
    family = models.ForeignKey(Family, on_delete=models.DO_NOTHING, null=True, blank=True)
    scientific_name = models.ForeignKey(ScientificName, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.animal.name


class ConservationStatus(models.Model):
    class Meta:
        verbose_name = 'Conservation Status'
        verbose_name_plural = 'Conservation Statuses'
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.status


class Fact(models.Model):
    prey = models.CharField(max_length=100, null=True, blank=True)
    distinct_feature = models.CharField(max_length=100, null=True, blank=True)
    habitat = models.CharField(max_length=100, null=True, blank=True)
    diet = models.CharField(max_length=100, null=True, blank=True)
    average_litter_size = models.CharField(max_length=100, null=True, blank=True)
    lifestyle = models.CharField(max_length=100, null=True, blank=True)
    favourite_food = models.CharField(max_length=100, null=True, blank=True)
    group = models.CharField(max_length=100, null=True, blank=True)
    name_of_young = models.CharField(max_length=100, null=True, blank=True)
    group_behavior = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.animal.name


class PhysicalCharacteristics(models.Model):
    color = models.CharField(max_length=100, null=True, blank=True)
    skin_type = models.CharField(max_length=50, null=True, blank=True)
    top_speed = models.CharField(max_length=50, null=True, blank=True)
    lifespan = models.CharField(max_length=50, null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
   
    # def __str__(self):
    #     return self.animal.name


class Location(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    
class Animal(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    classification = models.OneToOneField(Classification, on_delete=models.DO_NOTHING, null=True, blank=True)
    conservation_status = models.ForeignKey(ConservationStatus, on_delete=models.DO_NOTHING, null=True, blank=True)
    facts = models.OneToOneField(Fact, on_delete=models.DO_NOTHING, null=True, blank=True)
    location = models.ManyToManyField(Location)
    locationimage = models.ImageField(upload_to="images/locations/", null=True)
    physical_characteristics = models.OneToOneField(PhysicalCharacteristics, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


    @property
    def locations(self):
        if self.location:
            return '\n '.join([i.name for i in self.location.all()])


class Image(models.Model):
    image = models.ImageField(upload_to='images/animals/')
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.animal.name

# class AnimalLocation(models.Model):
#     animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING, null=True, blank=True)
#     location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True, blank=True)