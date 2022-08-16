from django.contrib import admin
from apps.catalog.models import Category, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag_thumbnail']
    list_display_links = ['id', 'image_tag_thumbnail']
    fields = ['image_tag', 'image']
    readonly_fields = ['image_tag']


class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = Product.images.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'quantity', 'price']
    list_display = ['id', 'name', 'quantity', 'price']
    list_display_links = ['id', 'name', 'quantity', 'price']
    inlines = [ProductCategoryInline, ProductImageInline]
