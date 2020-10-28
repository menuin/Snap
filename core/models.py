from django.conf import settings
from django.db import models


class Couple(models.Model):
    name=models.CharField(max_length=20)
    yeombyung=0

    def __str__(self):
        return f"{self.name}"
        
    def lovelove(self):
        self.yeombyung+=1
        self.save()


""" class Thanos(models.Model):
    patience=10

    def snap(self):
        self.patience=10
        self.save() """

# Create your models here.
