from django.contrib import admin
from .models import Owner

# Register your models here.
# admin.site.register(Owner)

@admin.register(Owner)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id","nombre", "pais", "descripcion")