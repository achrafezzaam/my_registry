from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

category_router = DefaultRouter()
category_router.register(r'categories', CategoryViewSet)
