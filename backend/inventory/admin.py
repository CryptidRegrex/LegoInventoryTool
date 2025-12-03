from django.contrib import admin
from .models import (
    Theme,
    LegoSet,
    PartCategory,
    Part,
    Color,
    SetPart,
    InventoryItem,
)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(LegoSet)
class LegoSetAdmin(admin.ModelAdmin):
    list_display = ("set_num", "name", "theme", "year", "num_parts")
    list_filter = ("theme", "year")
    search_fields = ("set_num", "name")


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


@admin.register(SetPart)
class SetPartAdmin(admin.ModelAdmin):
    list_display = ("lego_set", "part", "color", "quantity")
    list_filter = ("lego_set", "color")
    search_fields = ("lego_set__set_num", "lego_set__name", "part__part_num", "part__name")


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("part", "color", "quantity", "location")
    list_filter = ("color", "location")
    search_fields = ("part__part_num", "part__name", "location")
