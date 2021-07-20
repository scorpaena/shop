from django.contrib import admin
from .models import Adjustment


class AdjustmentAdmin(admin.ModelAdmin):

    fields = (
        "procurement_price_lower_limit",
        "procurement_price_upper_limit",
        "extra_charge",
        "risk",
    )

    list_display = (
        "procurement_price_lower_limit",
        "procurement_price_upper_limit",
        "extra_charge",
        "risk",
    )


admin.site.register(Adjustment, AdjustmentAdmin)
