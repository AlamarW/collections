from django.urls import path

from . import views

urlpatterns = [
    path("api/collections/", views.collection_list, name="collection_list"),
    path("api/collection/<int:pk>", views.collection_detail, name="collection_detail"),
]
