from rest_framework import serializers
from .models import Product


class ProductEditorSerializer(serializers.ModelSerializer):

    procurement_price = serializers.DecimalField(
        max_digits=6, decimal_places=1, min_value=0, default=1.0
    )
    tax = serializers.DecimalField(
        max_digits=2, decimal_places=1, min_value=0, default=None
    )
   
    class Meta:
        model = Product
        fields = ["id", "name", "procurement_price", "tax"]


class ProductViewerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = ["id", "name", "sticker_price"]
        read_only_fields = ["id", "name", "sticker_price"]