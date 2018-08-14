import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Licence(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nom du permis')

    class Meta:
        verbose_name = "Permis"
        verbose_name_plural = "Permis"


    def __str__(self):
        return self.name

class Composition(models.Model):
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE, verbose_name='Permis associé')
    name = models.CharField(max_length=200, verbose_name='Nom de la formule')

    class Meta:
        verbose_name = "Formule"

    def __str__(self):
        return self.name

class ItemComposition(models.Model):
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item
