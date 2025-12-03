from django.db import models
from django.conf import settings


class PartCategory(models.Model):
    """Categories like Bricks, Plates, Tiles, Minifig Accessories, etc."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Part(models.Model):
    """Represents a Lego part design (ignoring color)."""
    part_num = models.CharField(max_length=50, unique=True)  # e.g. "3001"
    name = models.CharField(max_length=200)
    category = models.ForeignKey(PartCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.part_num} - {self.name}"


class Color(models.Model):
    """Lego color (e.g., 'Bright Red', 'Black')."""
    name = models.CharField(max_length=100, unique=True)
    rgb = models.CharField(max_length=6, blank=True)  # hex RGB without '#', e.g. "FF0000"
    is_transparent = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    """
    Represents a specific quantity of a part+color that you actually own.
    """
    owner = models.ForeignKey(               
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventory_items",
    )
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    location = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional location label, e.g. 'Bin A1', 'Drawer 3'"
    )
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("part", "color", "location")

    def __str__(self):
        loc = f" @ {self.location}" if self.location else ""
        return f"{self.quantity} x {self.part} ({self.color}){loc}"
