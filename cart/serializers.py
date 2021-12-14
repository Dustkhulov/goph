from rest_framework import serializers
from .models import *


class CardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    carditems = CardItemSerializer(read_only=True, many=True)

    class Meta:
        model = Orders
        fields = '__all__'