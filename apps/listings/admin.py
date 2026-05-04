from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'price', 'category', 'status', 'created_at')
    list_filter = ('category', 'status', 'location_type', 'condition')
    search_fields = ('title', 'description', 'seller__username')