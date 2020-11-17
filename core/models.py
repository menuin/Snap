from django.conf import settings
from django.db import models
from django.utils import timezone


class Couple(models.Model):
    name=models.CharField(max_length=20)
    love=models.IntegerField(default=0)
    choice=models.IntegerField(default=0)
    snapped=models.IntegerField(default=0)
    created_date=models.DateTimeField(
        default=timezone.now
    )
    photo=models.ImageField(blank=True, null=True, upload_to="core/images")

    def __str__(self):
        return f"{self.name}"



# Create your models here.
