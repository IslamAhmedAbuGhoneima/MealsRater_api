from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RateSerializer