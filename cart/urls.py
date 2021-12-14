from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('orders/<int:pk>', OrderViewRetrieve.as_view()),
    path('cart/', CardView.as_view()),
    path('cart/<int:pk>', CardViewRetrieve.as_view()),
]