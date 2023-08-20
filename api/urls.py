from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('meals',views.MealViewSet)
router.register('rate',views.RateViewSet)
router.register('users',views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]