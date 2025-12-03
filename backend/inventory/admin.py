from django.contrib import admin
from .models import (
    PartCategory,
    Part,
    Color,
    InventoryItem,
)

@admin.register(PartCategory)
class PartCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ("part_num", "name", "category")
    list_filter = ("category",)
    search_fields = ("part_num", "name")


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "rgb", "is_transparent")
    list_filter = ("is_transparent",)
    search_fields = ("name",)


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("owner", "part", "color", "quantity", "location")
    list_filter = ("owner", "color", "location")
    search_fields = (
        "owner__username",
        "part__part_num",
        "part__name",
        "location",
    )