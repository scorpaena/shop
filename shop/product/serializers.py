from rest_framework import serializers
from .models import Product
from .validators import ProductTaxValidation


class ProductSerializerEditor(serializers.ModelSerializer):

    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tax = serializers.IntegerField()
    
    class Meta:
        model = Product
        fields = ["id", "name", "procurement_price", "tax"]
        read_only_fields = ["name", "procurement_price"]
        validators = [
            ProductTaxValidation(),
        ]


class ProductSerializerViewer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = ["id", "name", "sticker_price"]