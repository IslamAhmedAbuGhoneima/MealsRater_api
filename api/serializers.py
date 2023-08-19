from rest_framework.serializers import ModelSerializer
from .models import *
class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class RateSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'