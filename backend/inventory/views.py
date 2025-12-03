# inventory/views.py

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from rest_framework import viewsets, permissions

from .forms import SignUpForm
from .models import (
    InventoryItem,
    PartCategory,
    Part,
    Color,
)
from .serializers import (
    PartCategorySerializer,
    PartSerializer,
    ColorSerializer,
    InventoryItemSerializer,
)


# ---------- HTML views ----------

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after signup
            return redirect("inventory:inventory_list")
    else:
        form = SignUpForm()
    return render(request, "inventory/signup.html", {"form": form})


@login_required
def inventory_list(request):
    items = (
        InventoryItem.objects
        .select_related("part", "color")
        .filter(owner=request.user)
        .order_by("part__part_num", "color__name")
    )
    return render(request, "inventory/inventory_list.html", {"items": items})


# ---------- API viewsets (DRF) ----------

class PartCategoryViewSet(viewsets.ModelViewSet):
    queryset = PartCategory.objects.all().order_by("name")
    serializer_class = PartCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all().order_by("part_num")
    serializer_class = PartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all().order_by("name")
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    API for a user's inventory.
    Each user only sees / modifies their own items.
    """
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show inventory items belonging to the logged-in user
        return (
            InventoryItem.objects
            .select_related("part", "color")
            .filter(owner=self.request.user)
        )

    def perform_create(self, serializer):
        # Force owner to be the current user
        serializer.save(owner=self.request.user)
