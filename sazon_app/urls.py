from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import gerenteViewSet, inventarioViewSet


router = DefaultRouter()
router.register (r'gerente', gerenteViewSet)
router.register (r'inventario', inventarioViewSet)


urlpatterns = [
    path('api', include(router.urls)),
]

