from rest_framework.exceptions import ValidationError


class ProductTaxValidation:
    def __call__(self, attrs):
        if attrs['tax'] < 0:
            return ValidationError("tax cannot be negative")
