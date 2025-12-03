from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("inventory/", views.inventory_list, name="inventory_list"),

    # you can make the home page redirect to inventory if you like
    path("", views.inventory_list, name="home"),
]

