from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    procurement_price = models.PositiveIntegerField(default=1)
    extra_charge = models.PositiveIntegerField(default=0)
    tax = models.PositiveIntegerField(default=0)

    @property
    def sticker_price(self):
        price = self.procurement_price*(1+(self.tax+self.extra_charge)/100)
        return round(price)

    @property
    def item_margin(self):
        margin = (1-self.procurement_price/self.sticker_price)*100
        return round(margin)

    def __str__(self):
        return self.name
