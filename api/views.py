from django.shortcuts import render
from rest_framework import viewsets ,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .models import *
from .serializers import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        print(token)
        return Response({
                'token': token.key, 
                }, 
            status=status.HTTP_201_CREATED)
    
    # def list(self, request, *args, **kwargs):
    #     response = {'message': 'You cant create rating like that'}
    #     return Response(response, status=status.HTTP_400_BAD_REQUEST)


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @action(methods=['POST'],detail=True)
    def rate_meal(self,request,pk):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            # for authenticated only
            # username = request.data['username']
            # user = User.objects.get(username = username)
            user = request.user
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        return Response({
            'message':'wrong way to update'
        },status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        return Response({
            'message':'wrong way to create'
        },status=status.HTTP_400_BAD_REQUEST)