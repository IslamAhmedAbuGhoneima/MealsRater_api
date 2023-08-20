from rest_framework.serializers import ModelSerializer
from .models import *
class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','title','description','no_of_rating','avg_rating']

class RateSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'