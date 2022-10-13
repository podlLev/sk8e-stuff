from django.contrib import admin
from apps.main.models import Page, ProductSet, GlobalSetting
from adminsortable2.admin import SortableAdminMixin


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    list_display_links = ['id', 'name']
    readonly_fields = ['slug']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ProductSetProductsInline(admin.TabularInline):
    model = ProductSet.products.through
    extra = 1


@admin.register(ProductSet)
class ProductSetAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['sort', 'id', 'name', 'is_active']
    list_display_links = ['id', 'name']
    fields = ['name', 'is_active']
    inlines = [ProductSetProductsInline]


@admin.register(GlobalSetting)
class GlobalSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
