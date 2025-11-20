from django.urls import path

from . import views

urlpatterns = [
    path("api/collections/", views.collection_list, name="collection_list"),
    path(
        "api/collections/<int:pk>/", views.collection_detail, name="collection_detail"
    ),
    path(
        "api/collections/<int:collection_pk>/items/", views.item_list, name="item_list"
    ),
    path(
        "api/collections/<int:collection_pk>/items/<int:pk>/",
        views.item_detail,
        name="item_detail",
    ),
]
