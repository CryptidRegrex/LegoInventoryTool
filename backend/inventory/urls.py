from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ThemeViewSet,
    LegoSetViewSet,
    PartCategoryViewSet,
    PartViewSet,
    ColorViewSet,
    SetPartViewSet,
    InventoryItemViewSet,
)

router = DefaultRouter()
router.register(r"themes", ThemeViewSet)
router.register(r"sets", LegoSetViewSet, basename="lego-set")
router.register(r"part-categories", PartCategoryViewSet)
router.register(r"parts", PartViewSet)
router.register(r"colors", ColorViewSet)
router.register(r"set-parts", SetPartViewSet)
router.register(r"inventory", InventoryItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
