from django.db import models


# Create your models here.
ORIGIN = (
    ('AS', 'Azja'),
    ('EU', 'Europa'),
    ('NA', 'Ameryka Płn.'),
)


SHAPES1 = (
    ("drzewo", "drzewo"),
    ("krzew", "krzew"),
    ("niewysokie drzewo", "niewysokie drzewo"),
    ("niewysokie drzewo lub krzew", "niewysokie drzewo lub krzew"),
)


COLORS = (
    ("zielony", "zielony"),
    ("czerwony", "czerwony"),
    ("żółty", "żółty"),
    ("pomarańczowy", "pomarańczowy"),
    ("pstry", "pstry"),
)


FROST_RES = (
    ("całkowicie mrozoodporny", "całkowicie mrozoodporny"),
    ("mrozoodporny", "mrozoodporny"),
    ("nie w pełni odporny - przemarza podczas surowych zim", "nie w pełni odporny - przemarza podczas surowych zim"),
)


class Acers(models.Model):
    uid = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    tstamp = models.IntegerField()
    crdate = models.IntegerField()
    cruser_id = models.IntegerField()
    sorting = models.IntegerField()
    deleted = models.IntegerField()
    hidden = models.IntegerField()
    botanic_name = models.CharField(max_length=113, blank=True)
    latin_name = models.CharField(max_length=113, blank=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    variant = models.CharField(max_length=90, blank=True, null=True)
    other_names = models.CharField(max_length=113, blank=True, null=True)
    origin1 = models.CharField(choices=ORIGIN, max_length=3, blank=True, null=True)
    origin2 = models.TextField(blank=True, null=True)
    occurrence = models.TextField(blank=True, null=True)
    image_tree = models.TextField(blank=True, null=True)
    image_bark = models.TextField(blank=True, null=True)
    image_leaf = models.TextField(blank=True, null=True)
    in_poland = models.TextField(blank=True, null=True)
    height_10 = models.CharField(max_length=45, blank=True, null=True)
    shape1 = models.CharField(choices=SHAPES1, max_length=90, blank=True, null=True)
    shape2 = models.TextField(blank=True, null=True)
    leaf_structure = models.TextField(blank=True, null=True)
    leaf_size = models.CharField(max_length=150, blank=True, null=True)
    lc_spring1 = models.CharField(choices=COLORS, max_length=45, blank=True, null=True)
    lc_spring2 = models.TextField(blank=True, null=True)
    lc_summer1 = models.CharField(choices=COLORS, max_length=45, blank=True, null=True)
    lc_summer2 = models.TextField(blank=True, null=True)
    lc_autumn1 = models.CharField(choices=COLORS, max_length=45, blank=True, null=True)
    lc_autumn2 = models.TextField(blank=True, null=True)
    leaf_tail = models.CharField(max_length=150, blank=True, null=True)
    bark = models.TextField(blank=True, null=True)
    flowers = models.TextField(blank=True, null=True)
    fruits = models.TextField(blank=True, null=True)
    frost_res = models.TextField(choices=FROST_RES, blank=True, null=True)
    frost_res_zones = models.CharField(max_length=8, blank=True, null=True)
    characteristics = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stand = models.TextField(blank=True, null=True)
    soil_kind = models.CharField(max_length=75, blank=True, null=True)
    soil_ph = models.CharField(max_length=75, blank=True, null=True)
    height_max1 = models.IntegerField(blank=True, null=True)
    height_max2 = models.IntegerField(blank=True, null=True)
    other_botanic_name1 = models.CharField(max_length=113, blank=True, null=True)
    other_botanic_name2 = models.CharField(max_length=113, blank=True, null=True)
    other_latin_name = models.CharField(max_length=113, blank=True, null=True)
    other_variant = models.CharField(max_length=90, blank=True, null=True)
    poland_availability = models.IntegerField(blank=True, null=True)
    new_image_tree = models.ImageField(upload_to='tree', blank=True, null=True)
    new_image_bark = models.ImageField(upload_to='bark', blank=True, null=True)
    new_image_leaf = models.ImageField(upload_to='leaf', blank=True, null=True)

    def __str__(self):
        return self.latin_name
