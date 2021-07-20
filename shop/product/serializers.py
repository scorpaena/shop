from rest_framework import serializers
from .models import Product


class ProductEditorSerializer(serializers.ModelSerializer):

    procurement_price = serializers.DecimalField(
        max_digits=7,
        decimal_places=1,
        min_value=0.1,
    )
    tax = serializers.DecimalField(
        max_digits=3, decimal_places=1, min_value=0.0, default=None
    )

    class Meta:
        model = Product
        fields = ["id", "name", "procurement_price", "tax"]


class ProductViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "sticker_price"]
