from django.db import models
from category.models import Subcategory

# Create your models here.


class Product(models.Model):
    name = models.CharField(verbose_name='Product name', max_length=100, unique=True)
    company = models.CharField(verbose_name='Company', max_length=200)
    description = models.TextField(verbose_name='Description')
    price = models.IntegerField(verbose_name='Price')
    image = models.ImageField(verbose_name='Image', upload_to='static/products')
    number = models.IntegerField(verbose_name='Number_products', blank=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    output_form = models.CharField(max_length=100, blank=True)
    substance_type = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name