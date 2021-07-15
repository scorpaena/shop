from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    procurement_price = models.PositiveIntegerField(default=1)
    extra_charge = models.PositiveIntegerField(default=0)
    tax = models.PositiveIntegerField(default=0)

    @property
    def sticker_price(self):
        return self.procurement_price*(1+(self.tax+self.extra_charge)/100)

    @property
    def item_margin(self):
        return (1-self.procurement_price/self.sticker_price)*100

    # @property
    # def extra_charge(self):
    #     return self.extra_charge

    # @property
    # def tax_per_item(self):
    #     return self.tax_per_item

    # @property
    # def tax_for_all(self):
    #     return self.tax_for_all

    # @property
    # def risk(self):
    #     pass

    # def apply_tax_per_item(self):
    #     self.sticker_price += self.sticker_price*self.tax_per_item/100
    #     return self.sticker_price 

    # def save(self, *args, **kwargs):
    #     self.apply_tax_per_item()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

