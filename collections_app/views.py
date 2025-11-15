import json

from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Collection


@csrf_exempt
def collection_list(request):
    # get collections where user == request
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)
    if request.method == "GET":
        collections = Collection.objects.filter(owner=request.user)
        collections_data = [
            {
                "id": collection.id,
                "name": collection.name,
            }
            for collection in collections
        ]
        return JsonResponse(collections_data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        collection = Collection.objects.create(name=data["name"], owner=request.user)
        return JsonResponse({"id": collection.id, "name": collection.name}, status=201)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def collection_detail(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    if request.method == "GET":
        collection = get_object_or_404(Collection, pk=pk, owner=request.user)
        collection_data = {
            "id": collection.id,
            "name": collection.name,
        }

        return JsonResponse(collection_data)
