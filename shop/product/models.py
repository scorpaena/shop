from django.db import models
from constance import config
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=250)
    procurement_price = models.DecimalField(max_digits=6, decimal_places=1, default=1.0)
    extra_charge = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    tax = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    risk = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    @property
    def sticker_price(self):
        procurement_price = self.procurement_price
        extra_charge = self.get_extra_charge()
        tax = self.get_tax()
        risk = self.get_risk()
        price = procurement_price*Decimal(1+(extra_charge+tax+risk)/100)
        return round(price, 1)

    @property
    def item_margin(self):
        procurement_price = self.procurement_price
        sticker_price = self.sticker_price
        try:
            margin = (1-procurement_price/sticker_price)*100
        except ZeroDivisionError:
            return 0
        return round(margin, 1)

    def get_extra_charge(self):
        if self.extra_charge is not None:
            return self.extra_charge
        return config.EXTRA_CHARGE

    def get_tax(self):
        if self.tax is not None:
            return self.tax
        return config.TAX

    def get_risk(self):
        if self.risk is not None:
            return self.risk
        return config.RISK

    def __str__(self):
        return self.name
