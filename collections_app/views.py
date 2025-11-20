import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Collection, Item


@csrf_exempt
def collection_list(request):
    """
    Methods for interacting with a list of collections
    So far the only Method that makes sense at this level is GET
    """

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)
    # get collections where user == request
    if request.method == "GET":
        collections = Collection.objects.filter(owner=request.user)  # pyright: ignore[reportAttributeAccessIssue]
        collections_data = [
            {
                "id": collection.id,
                "name": collection.name,
                "collection_items": [item.id for item in collection.items.all()],
                "description": collection.description,
                "collection_schema": collection.collection_schema,
            }
            for collection in collections
        ]
        return JsonResponse(collections_data, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def collection_detail(request, pk):
    """
    Create, Read, Update or Delete a single collection.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    # Create a collection for the user
    elif request.method == "POST":
        data = json.loads(request.body)
        collection = Collection.objects.create(name=data["name"], owner=request.user)  # pyright: ignore[reportAttributeAccessIssue]
        return JsonResponse({"id": collection.id, "name": collection.name}, status=201)

    # Read a collection for the user
    if request.method == "GET":
        collection = get_object_or_404(Collection, pk=pk, owner=request.user)
        collection_data = {
            "id": collection.id,
            "name": collection.name,
            "collection_items": [item.id for item in collection.items.all()],
            "description": collection.description,
            "collection_schema": collection.collection_schema,
        }
        return JsonResponse(collection_data)

    # Update a collection for the user
    elif request.method == "PUT":
        data = json.loads(request.body)
        collection = get_object_or_404(Collection, pk=pk, owner=request.user)
        collection.name = data.get("name", collection.name)
        if "description" in data:
            collection.description = data["description"]
        if "collection_schema" in data:
            collection.collection_schema = data["collection_schema"]
        # Note: collection_items are managed through Item.item_collection ForeignKey
        # Cannot directly set items from collection side
        collection.save()
        return JsonResponse({"id": collection.id, "name": collection.name}, status=200)

    # Delete collection from the user's collection list
    elif request.method == "DELETE":
        collection = get_object_or_404(Collection, pk=pk, owner=request.user)
        collection.delete()
        return JsonResponse({"message": "Collection deleted"}, status=200)


@csrf_exempt
def item_list(request, collection_pk):
    """
    Methods for interacting with a list of items in a collection
    So far the only Method that makes sense at this level is GET
    """

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    # Verify the collection exists and belongs to the user
    collection = get_object_or_404(Collection, pk=collection_pk, owner=request.user)

    # get items for this specific collection
    if request.method == "GET":
        items = Item.objects.filter(item_collection=collection)
        items_data = [
            {
                "id": item.id,
                "name": item.name,
                "item_data": item.item_data,
                "item_collection": item.item_collection.id,
            }
            for item in items
        ]
        return JsonResponse(items_data, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def item_detail(request, collection_pk, pk):
    """
    Create, Read, Update or Delete a single item.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    # Verify the collection exists and belongs to the user
    collection = get_object_or_404(Collection, pk=collection_pk, owner=request.user)

    # Create an item for the collection
    if request.method == "POST":
        data = json.loads(request.body)
        item = Item.objects.create(
            name=data["name"],
            item_data=data.get("item_data", {}),
            item_collection=collection,
        )
        return JsonResponse(
            {
                "id": item.id,
                "name": item.name,
                "item_data": item.item_data,
                "item_collection": item.item_collection.id,
            },
            status=201,
        )

    # Read an item from the collection
    elif request.method == "GET":
        item = get_object_or_404(Item, pk=pk, item_collection=collection)
        item_data = {
            "id": item.id,
            "name": item.name,
            "item_data": item.item_data,
            "item_collection": item.item_collection.id,
        }
        return JsonResponse(item_data)

    # Update an item in the collection
    elif request.method == "PUT":
        data = json.loads(request.body)
        item = get_object_or_404(Item, pk=pk, item_collection=collection)
        item.name = data.get("name", item.name)
        if "item_data" in data:
            item.item_data = data["item_data"]
        item.save()
        return JsonResponse(
            {
                "id": item.id,
                "name": item.name,
                "item_data": item.item_data,
                "item_collection": item.item_collection.id,
            },
            status=200,
        )

    # Delete item from the collection
    elif request.method == "DELETE":
        item = get_object_or_404(Item, pk=pk, item_collection=collection)
        item.delete()
        return JsonResponse({"message": "Item deleted"}, status=200)
