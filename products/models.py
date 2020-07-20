from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True)
    # (auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product_details', args=(self.id,))

    def __str__(self):
        return self.title
