from django.urls import path
from .views import *


urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/<int:pk>', ProductCreateDeleteView.as_view()),
]