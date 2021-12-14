from django.urls import path
from .views import *


urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view()),
    path('subcategory/', SubcategoryListView.as_view()),
    path('subcategory/<int:pk>', SubcategoryDetailView.as_view()),
]