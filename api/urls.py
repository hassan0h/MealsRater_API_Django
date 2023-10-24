from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RatigViewSet


router = routers.DefaultRouter()
router.register('meals', MealViewSet)
router.register('rating', RatigViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]