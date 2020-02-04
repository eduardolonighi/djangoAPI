from django.db import models

class Item(models.Model):
  title= models.CharField(max_length=250)
  description = models.CharField(max_length=500)

  def __str__(self):
    return self.title