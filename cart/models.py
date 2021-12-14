from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
# Create your models here.


class Orders(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="cards", on_delete=models.PROTECT, default=None)
    is_sold = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.added_date}"


class Card(models.Model):
    product = models.ForeignKey(Product, related_name="carditems", on_delete=models.PROTECT, default=None)
    total = models.IntegerField(default=1)
    card = models.ForeignKey(Orders, related_name="carditems", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.product.name