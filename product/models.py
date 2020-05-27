from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    num_of_sales = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    short_description = models.CharField(max_length=300)
    long_description = models.CharField(max_length=500)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return self.name


