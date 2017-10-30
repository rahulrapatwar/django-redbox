from django.db import models

# Create your models here.
class Cart(models.Model):
    product = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()

    def __str__(self):
        return self.product
