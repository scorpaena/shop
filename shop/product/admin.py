from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):

    fields = (
        "name",
        "procurement_price",
        "extra_charge",
        "tax",
        "risk",
        "sticker_price",
        "item_margin",
    )
    readonly_fields = (
        "sticker_price",
        "item_margin",
    )
    list_display = (
        "name",
        "procurement_price",
        "extra_charge",
        "tax",
        "risk",
        "sticker_price",
        "item_margin",
    )


admin.site.register(Product, ProductAdmin)
