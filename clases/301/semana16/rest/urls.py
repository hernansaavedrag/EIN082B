from rest_framework import routers
from .views import CarreraViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('carreras',CarreraViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
