from rest_framework import serializers
from .models import Theme, LegoSet, PartCategory, Part, Color, SetPart, InventoryItem


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class LegoSetSerializer(serializers.ModelSerializer):
    theme = ThemeSerializer(read_only=True)
    theme_id = serializers.PrimaryKeyRelatedField(
        source="theme", queryset=Theme.objects.all(), write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = LegoSet
        fields = ["id", "set_num", "name", "year", "num_parts", "theme", "theme_id"]


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


class SetPartSerializer(serializers.ModelSerializer):
    lego_set = LegoSetSerializer(read_only=True)
    lego_set_id = serializers.PrimaryKeyRelatedField(
        source="lego_set", queryset=LegoSet.objects.all(), write_only=True
    )

    part = PartSerializer(read_only=True)
    part_id = serializers.PrimaryKeyRelatedField(
        source="part", queryset=Part.objects.all(), write_only=True
    )

    color = ColorSerializer(read_only=True)
    color_id = serializers.PrimaryKeyRelatedField(
        source="color", queryset=Color.objects.all(), write_only=True, allow_null=True, required=False
    )

    class Meta:
        model = SetPart
        fields = [
            "id",
            "lego_set", "lego_set_id",
            "part", "part_id",
            "color", "color_id",
            "quantity",
        ]


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
