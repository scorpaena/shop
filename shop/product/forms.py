from django.contrib.admin.helpers import ActionForm
from django import forms


class ApplyForAllForm(ActionForm):
    tax_for_all = forms.IntegerField(initial=0)
    extra_charge_for_all = forms.IntegerField(initial=0)
    risk_for_all = forms.IntegerField(initial=0)
