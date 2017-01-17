from django.db import models

# Create your models here.
class Acers(models.Model):
    uid = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    tstamp = models.IntegerField()
    crdate = models.IntegerField()
    cruser_id = models.IntegerField()
    sorting = models.IntegerField()
    deleted = models.IntegerField()
    hidden = models.IntegerField()
    botanic_name = models.CharField(max_length=113)
    latin_name = models.CharField(max_length=113)
    type = models.CharField(max_length=45)
    variant = models.CharField(max_length=90)
    other_names = models.CharField(max_length=113)
    origin1 = models.CharField(max_length=3)
    origin2 = models.TextField()
    occurrence = models.TextField()
    image_tree = models.TextField()
    image_bark = models.TextField()
    image_leaf = models.TextField()
    in_poland = models.TextField()
    height_10 = models.CharField(max_length=45)
    shape1 = models.CharField(max_length=90)
    shape2 = models.TextField()
    leaf_structure = models.TextField()
    leaf_size = models.CharField(max_length=150)
    lc_spring1 = models.CharField(max_length=45)
    lc_spring2 = models.TextField()
    lc_summer1 = models.CharField(max_length=45)
    lc_summer2 = models.TextField()
    lc_autumn1 = models.CharField(max_length=45)
    lc_autumn2 = models.TextField()
    leaf_tail = models.CharField(max_length=150)
    bark = models.TextField()
    flowers = models.TextField()
    fruits = models.TextField()
    frost_res = models.TextField()
    frost_res_zones = models.CharField(max_length=8)
    characteristics = models.TextField()
    description = models.TextField()
    stand = models.TextField()
    soil_kind = models.CharField(max_length=75)
    soil_ph = models.CharField(max_length=75)
    height_max1 = models.IntegerField(blank=True, null=True)
    height_max2 = models.IntegerField(blank=True, null=True)
    other_botanic_name1 = models.CharField(max_length=113)
    other_botanic_name2 = models.CharField(max_length=113)
    other_latin_name = models.CharField(max_length=113)
    other_variant = models.CharField(max_length=90)
    poland_availability = models.IntegerField(blank=True, null=True)
    new_image_tree = models.ImageField(upload_to='tree')
    new_image_bark = models.ImageField(upload_to='bark')
    new_image_leaf = models.ImageField(upload_to='leaf')

    def __str__(self):
        return self.name

