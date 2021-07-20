from django.db import models


class Adjustment(models.Model):
    procurement_price_lower_limit = models.DecimalField(
        max_digits=7, decimal_places=1, default=1.0
    )
    procurement_price_upper_limit = models.DecimalField(
        max_digits=7, decimal_places=1, default=1.0
    )
    extra_charge = models.DecimalField(max_digits=4, decimal_places=1)
    risk = models.DecimalField(max_digits=3, decimal_places=1)
