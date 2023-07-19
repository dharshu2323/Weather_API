from django.db import models

# Create your models here.
class city(models.Model):
    name=models.CharField(max_length=50,default="")
    def __str__(self) :
        return self.name
