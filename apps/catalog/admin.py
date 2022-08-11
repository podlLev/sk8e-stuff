from django.contrib import admin
from apps.catalog.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity', 'price', 'created_at']
    list_display_links = ['id', 'name', 'quantity', 'price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
