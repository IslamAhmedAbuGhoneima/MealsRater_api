from django.shortcuts import render
from rest_framework import viewsets ,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    @action(methods=['POST'],detail=True)
    def rate_meal(self,request,pk):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            username = request.data['username']
            user = User.objects.get(username = username)
            stars = request.data['stars']
            try:
                rate = Rating.objects.get(user=user.id,meal=meal.id)
                rate.stars = stars
                rate.save()
                serializer = RateSerializer(rate)
                json = {
                    'message':'Meal Rate Updated',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
            except:
                rate = Rating.objects.create(
                    user = user,
                    meal = meal,
                    stars = stars
                )
                serializer = RateSerializer(rate)
                json = {
                    'message':'Meal Rate Created',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
        else:
            json = {
                'message':'Stars not provided'
            }
            return Response(json,status=status.HTTP_400_BAD_REQUEST)

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RateSerializer