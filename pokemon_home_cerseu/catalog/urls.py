from django.urls import path
from . import views

urlpatterns = [
    path("catalog_list/", views.list_catalog, name="catalog_list")
]