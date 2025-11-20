from django.contrib import admin

from .models import Collection, Item


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    fields = ["name", "item_data"]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "description"]
    list_filter = ["owner"]
    search_fields = ["name", "description"]
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "item_collection", "get_owner"]
    list_filter = ["item_collection"]
    search_fields = ["name"]

    def get_owner(self, obj):
        return obj.item_collection.owner

    get_owner.short_description = "Owner"
