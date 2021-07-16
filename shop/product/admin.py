from django.contrib import admin
from django.db.models import F
from .models import Product
from .forms import ApplyForAllForm
from django.contrib import messages


class ProductAdmin(admin.ModelAdmin):
    
    def apply_extra_parameters(modeladmin, request, queryset):
        try:
            tax_for_all = int(request.POST['tax_for_all'])
            extra_charge_for_all = int(request.POST['extra_charge_for_all'])
            risk_for_all = int(request.POST['risk_for_all'])
        except ValueError:
            return messages.add_message(
                request, messages.ERROR, 'values must be positive integers'
            )
        else:
            if tax_for_all<0 or extra_charge_for_all<0 or risk_for_all<0 or risk_for_all>=100:
                return messages.add_message(
                    request, messages.ERROR, 
                    'values must be positive and "risk_for_all" must be < 100'
                )
            else:
                queryset.update(tax=F('tax')+tax_for_all)
                queryset.update(
                    extra_charge=F('extra_charge')*round((1/(1-risk_for_all/100)))
                    +extra_charge_for_all
                )


    action_form = ApplyForAllForm
    actions = [apply_extra_parameters,]
    fields = ('name', 'procurement_price', 'tax', 'extra_charge', 'sticker_price', 'item_margin',)
    readonly_fields = ('sticker_price', 'item_margin',)
    list_display = ('name', 'procurement_price', 'tax', 'extra_charge', 'sticker_price', 'item_margin',)

admin.site.register(Product, ProductAdmin)
