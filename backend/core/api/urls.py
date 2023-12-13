from rest_framework.routers import DefaultRouter
from categories.api.urls import category_router
from items.api.urls import item_router
from django.urls import path, include

router = DefaultRouter()

# Categories
router.registry.extend(category_router.registry)

# Items
router.registry.extend(item_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
