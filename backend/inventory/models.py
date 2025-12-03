from django.db import models


class Theme(models.Model):
    """High-level groups like Star Wars, City, Technic, etc."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class LegoSet(models.Model):
    """Represents a Lego set (like 75300 Imperial TIE Fighter)."""
    set_num = models.CharField(max_length=20, unique=True)  # e.g. "75300"
    name = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    num_parts = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.set_num} - {self.name}"


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


class SetPart(models.Model):
    """
    Relationship between a Lego set and the parts it uses.
    This lets you ask 'what parts do I need to build set X?'
    """
    lego_set = models.ForeignKey(LegoSet, on_delete=models.CASCADE, related_name="set_parts")
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ("lego_set", "part", "color")

    def __str__(self):
        return f"{self.lego_set.set_num}: {self.quantity} x {self.part} ({self.color or 'any color'})"


class InventoryItem(models.Model):
    """
    Represents a specific quantity of a part+color that you actually own.
    """
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
