from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.model_name} ({self.brand.name})"

