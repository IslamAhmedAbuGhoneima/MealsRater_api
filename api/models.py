from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=360)
    def no_of_rating(self):
        return Rating.objects.filter(meal = self).count()
    def avg_rating(self):
        avg_rate = 0
        count = self.no_of_rating()
        for start in range(count):
            avg_rate += Rating.objects.filter(meal = self)[start].stars
        return avg_rate/count if count > 0 else 0
    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    stars = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    def __str__(self):
        return self.meal.title
    class Meta:
        unique_together = (('user','meal'))
        index_together = (('user','meal'))