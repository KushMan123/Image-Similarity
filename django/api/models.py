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
    classification_for = models.CharField(max_length=50, null=True, blank=True)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.DO_NOTHING, null=True, blank=True)
    phylum = models.ForeignKey(Phylum, on_delete=models.DO_NOTHING, null=True, blank=True)
    class_name = models.ForeignKey(ClassName, on_delete=models.DO_NOTHING, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=True, blank=True)
    genus = models.ForeignKey(Genus, on_delete=models.DO_NOTHING, null=True, blank=True)
    family = models.ForeignKey(Family, on_delete=models.DO_NOTHING, null=True, blank=True)
    scientific_name = models.ForeignKey(ScientificName, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        if self.classification_for is not None:
            return self.classification_for


class ConservationStatus(models.Model):
    class Meta:
        verbose_name = 'Conservation Status'
        verbose_name_plural = 'Conservation Statuses'
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.status


class Fact(models.Model):
    facts_for = models.CharField(max_length=50, null=True, blank=True)
    main_prey = models.CharField(max_length=50, null=True, blank=True)
    distinct_feature = models.CharField(max_length=50, null=True, blank=True)
    habitat = models.CharField(max_length=50, null=True, blank=True)
    predators = models.CharField(max_length=50, null=True, blank=True)
    diet = models.CharField(max_length=50, null=True, blank=True)
    average_litter_size = models.CharField(max_length=50, null=True, blank=True)
    lifestyle = models.CharField(max_length=50, null=True, blank=True)
    favourite_food = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    slogan = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.facts_for


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
    # image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def locations(self):
        if self.location:
            return '\n '.join([i.name for i in self.location.all()])


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.animal

# class AnimalLocation(models.Model):
#     animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING, null=True, blank=True)
#     location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True, blank=True)