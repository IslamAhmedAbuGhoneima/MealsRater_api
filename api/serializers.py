from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {
            'password':{
                'write_only':True,
                'required':True
            }
        }

class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','title','description','no_of_rating','avg_rating']

class RateSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'