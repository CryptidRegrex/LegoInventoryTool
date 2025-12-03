from rest_framework import serializers
from .models import PartCategory, Part, Color, InventoryItem


class PartCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartCategory
        fields = "__all__"


class PartSerializer(serializers.ModelSerializer):
    category = PartCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=PartCategory.objects.all(), write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Part
        fields = ["id", "part_num", "name", "category", "category_id"]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class InventoryItemSerializer(serializers.ModelSerializer):
    part = PartSerializer(read_only=True)
    part_id = serializers.PrimaryKeyRelatedField(
        source="part", queryset=Part.objects.all(), write_only=True
    )

    color = ColorSerializer(read_only=True)
    color_id = serializers.PrimaryKeyRelatedField(
        source="color", queryset=Color.objects.all(), write_only=True
    )

    class Meta:
        model = InventoryItem
        fields = ["id", "part", "part_id", "color", "color_id", "quantity", "location", "notes"]
