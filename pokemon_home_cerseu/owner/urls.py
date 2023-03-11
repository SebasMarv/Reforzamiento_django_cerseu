from django.urls import path
from . import views

urlpatterns = [
    path("owner_list/", views.list_owner, name="owner_list"),
    path("owner_search/", views.search_owner, name="owner_search"),
    
    path("owner_delete/<int:id_owner>", views.owner_delete, name="owner_delete"),
    path("owner_update/<int:id_owner>", views.owner_edit, name="owner_update"),

    path("owner_list_class/", views.OwnerList.as_view(), name="owner_list_class"),
    path("owner_create/", views.OwnerCreate.as_view(), name="owner_create"),
    path("owner_update/<int:pk>", views.OwnerUpdate.as_view(), name="owner_update"),
    path("owner_delete_confirm/<int:pk>", views.OwnerDelete.as_view(), name="owner_delete_confirm"),
]