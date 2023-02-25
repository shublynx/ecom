from django.db import models

# Create your models here.


class Products(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField()
    dis_price = models.FloatField()
    category = models.CharField(max_length=100)
    descrip = models.TextField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.title