from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(verbose_name='Sub category', max_length=100)
    parent_id = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
