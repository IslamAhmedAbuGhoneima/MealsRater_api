from django.contrib import admin
from .models import *
# Register your models here.
class RateAdmin(admin.ModelAdmin):
    list_display = ['id','user','meal','stars']
    list_filter = ['user','meal']

class MealAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_filter = ['title','description']
    search_fields = ['title','description']
admin.site.register(Meal,MealAdmin)
admin.site.register(Rating,RateAdmin)
