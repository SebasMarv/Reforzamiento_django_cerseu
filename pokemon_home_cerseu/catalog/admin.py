from django.contrib import admin
from .models import Catalog

# Register your models here.
# admin.site.register(Catalog)

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id","garment", "classification", "price")