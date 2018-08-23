from django.db import models
from django.contrib.auth.models import User

class Spell(models.Model):
    spell_name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    incantation = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    reference = models.TextField()
    extract = models.TextField()
    extract_author = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg',blank=True)
    contributor = models.ForeignKey(User,default=None,on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.spell_name
