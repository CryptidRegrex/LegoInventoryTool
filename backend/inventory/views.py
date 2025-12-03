from rest_framework import viewsets
from .models import Theme, LegoSet, PartCategory, Part, Color, SetPart, InventoryItem
from .serializers import (
    ThemeSerializer,
    LegoSetSerializer,
    PartCategorySerializer,
    PartSerializer,
    ColorSerializer,
    SetPartSerializer,
    InventoryItemSerializer,
)


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all().order_by("name")
    serializer_class = ThemeSerializer


class LegoSetViewSet(viewsets.ModelViewSet):
    queryset = LegoSet.objects.all().order_by("set_num")
    serializer_class = LegoSetSerializer
    lookup_field = "id"  # could also use set_num if you want


class PartCategoryViewSet(viewsets.ModelViewSet):
    queryset = PartCategory.objects.all().order_by("name")
    serializer_class = PartCategorySerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all().order_by("part_num")
    serializer_class = PartSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all().order_by("name")
    serializer_class = ColorSerializer


class SetPartViewSet(viewsets.ModelViewSet):
    queryset = SetPart.objects.select_related("lego_set", "part", "color").all()
    serializer_class = SetPartSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.select_related("part", "color").all()
    serializer_class = InventoryItemSerializer
