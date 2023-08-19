from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('meals',views.MealViewSet)
router.register('rate',views.RateViewSet)

urlpatterns = [
    path('',include(router.urls))
]