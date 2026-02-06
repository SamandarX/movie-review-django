from django.contrib import admin
from .models import Item, Review


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'release_year')
    search_fields = ('title',)
    list_filter = ('category',)
    ordering = ('title',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'rating', 'created_at')
    search_fields = ('comment',)
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
