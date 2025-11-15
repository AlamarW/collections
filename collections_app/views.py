import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Collection


@csrf_exempt
def collection_list(request):
    """
    Methods for interacting with a list of collections
    So far the only Metho that makes sense at this level is GET
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
        }
        return JsonResponse(collection_data)

    # Update a collection for the user
    elif request.method == "PUT":
        data = json.loads(request.body)
        collection = get_object_or_404(Collection, pk=pk, owner=request.user)
        collection.name = data["name"]
        collection.save()
        return JsonResponse({"id": collection.id, "name": collection.name}, status=200)

    # Delete collection from the user's collection list
    elif request.method == "DELETE":
        data = json.loads(request.body)
        collection = get_object_or_404(Collection, pk=data["id"], owner=request.user)
        collection.delete()
        return JsonResponse({"message": "Collection deleted"}, status=200)
