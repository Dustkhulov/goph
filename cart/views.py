from rest_framework import generics
from .serializers import *
from .models import *


class CardView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardItemSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = CardSerializer


class OrderViewRetrieve(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = CardSerializer


class CardViewRetrieve(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardItemSerializer