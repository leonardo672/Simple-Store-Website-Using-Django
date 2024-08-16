from django.db import models

# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)

#class Movie(models.Model):
 #   name = models.CharField(max_length=200)
  #  image = models.CharField(max_length=2083)
  
    
   # image = models.ImageField(upload_to='Dishes/files/cover')

    