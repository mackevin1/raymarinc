from django.contrib import admin
from .models import Board


# Register your models here.
from django.contrib import admin
from products.models import Products
from products.models import Comment
from products.models import Board
admin.site.register(Products)
admin.site.register(Comment)
admin.site.register(Board)

from adminsortable2.admin import SortableAdminMixin
from shop.admin.product import CMSPageAsCategoryMixin, ProductImageInline
from .models import SmartCard


@admin.register(SmartCard)
class SmartCardAdmin(SortableAdminMixin, CMSPageAsCategoryMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('product_name', 'slug', 'product_code', 'unit_price', 'active', 'description',),
        }),
        (_("Properties"), {
            'fields': ('manufacturer', 'storage', 'card_type', 'speed',)
        }),
    )
    inlines = (ProductImageInline,)
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'product_code', 'unit_price', 'active',)
    search_fields = ('product_name',)
