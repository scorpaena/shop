from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from django import forms
from .models import Product

class TaxForAllForm(ActionForm):
    tax_for_all = forms.IntegerField(required=False)
    extra_charge_for_all = forms.IntegerField(required=False)
    risk_for_all = forms.IntegerField(required=False)


class ProductAdmin(admin.ModelAdmin):
    
    # @admin.action
    def apply_tax_for_all(modeladmin, request, queryset):
        tax_for_all = int(request.POST['tax_for_all'])
        tax_queryset = queryset.values_list('tax', flat=True)
        for tax in tax_queryset:
            tax += tax_for_all
            # tax.save()
        # queryset.update(tax=tax_queryset+tax_for_all)
    
    # @admin.action
    def apply_extra_charge_for_all(modeladmin, request, queryset):
        queryset.update(sticker_price=sticker_price*(1+extra_charge_for_all/100))

    # @admin.action
    def apply_risk_for_all(modeladmin, request, queryset):
        queryset.update(sticker_price=sticker_price*(1+risk_for_all/100))


    action_form = TaxForAllForm
    actions = [apply_tax_for_all, apply_extra_charge_for_all, apply_risk_for_all]
    fields = ('name', 'procurement_price', 'tax', 'extra_charge', 'sticker_price', 'item_margin',)
    readonly_fields = ('sticker_price', 'item_margin',)
    list_display = ('name', 'procurement_price', 'tax', 'extra_charge', 'sticker_price', 'item_margin',)
    # list_filter = ('author', 'title', 'content', 'date_posted')
    # search_fields = ('author__nickname', 'title', 'content', 'date_posted')
    # ordering = ('-date_posted',)





admin.site.register(Product, ProductAdmin)
