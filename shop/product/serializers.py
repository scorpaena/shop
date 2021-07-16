from rest_framework import serializers
from .models import Product


class ProductSerializerEditor(serializers.ModelSerializer):

    def validate(self, data):
        if data['procurement_price'] < 0 or data['tax'] < 0:
            raise serializers.ValidationError("numbers must be positive")
        return data
   
    class Meta:
        model = Product
        fields = ["id", "name", "procurement_price", "tax"]


class ProductSerializerViewer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = ["id", "name", "sticker_price"]