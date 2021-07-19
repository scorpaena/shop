from rest_framework import serializers
from .models import Product
from .validators import validate_field_value


class ProductEditorSerializer(serializers.ModelSerializer):

    def validate(self, data):
        validate_field_value(data, field='procurement_price')
        validate_field_value(data, field='tax')
        return super().validate(data)
   
    class Meta:
        model = Product
        fields = ["id", "name", "procurement_price", "tax"]


class ProductViewerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = ["id", "name", "sticker_price"]