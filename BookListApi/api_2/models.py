from django.db import models

class BookGenre(models.Model):
   name = models.CharField(max_length=255)
   slug = models.SlugField(max_length=255)
   
   def __str__(self):
       return self.name
   
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    inventory = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.ForeignKey(BookGenre, on_delete=models.CASCADE)