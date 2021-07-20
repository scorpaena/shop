from django.db import models
from constance import config
from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from adjustment.models import Adjustment


class Product(models.Model):
    name = models.CharField(max_length=250)
    procurement_price = models.DecimalField(max_digits=7, decimal_places=1)
    extra_charge = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True
    )
    tax = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    risk = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    @property
    def sticker_price(self):
        procurement_price = self.procurement_price
        extra_charge = self.get_extra_charge()
        tax = self.get_tax()
        risk = self.get_risk()
        sum_charge = Decimal(extra_charge + tax + risk)
        price = Decimal(procurement_price) * (1 + sum_charge / 100)
        return round(price, 1)

    @property
    def item_margin(self):
        procurement_price = self.procurement_price
        sticker_price = self.sticker_price
        try:
            margin = (1 - procurement_price / sticker_price) * 100
        except ZeroDivisionError:
            return 0
        return round(margin, 1)

    def get_extra_charge(self):
        if self.extra_charge is not None:
            return self.extra_charge
        elif self.get_adjustment_range() is not None:
            return self.get_adjustment_range().extra_charge
        return config.EXTRA_CHARGE

    def get_tax(self):
        if self.tax is not None:
            return self.tax
        return config.TAX

    def get_risk(self):
        if self.risk is not None:
            return self.risk
        elif self.get_adjustment_range() is not None:
            return self.get_adjustment_range().risk
        return config.RISK

    def get_adjustment_range(self):
        price = self.procurement_price
        try:
            adjustment = Adjustment.objects.filter(
                procurement_price_lower_limit__lt=price
            ).get(procurement_price_upper_limit__gte=price)
        except ObjectDoesNotExist:
            return None
        return adjustment

    def __str__(self):
        return self.name
