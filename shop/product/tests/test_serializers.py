import pytest
from product.serializers import ProductSerializerEditor

def test_product_data_is_valid(db):
    serializer = ProductSerializerEditor(
        data = {
            "name": "foo",
            "procurement_price": "1",
            "tax": "1",
        }
    )
    assert serializer.is_valid()

def test_product_procurement_price_is_invalid(db):
    serializer = ProductSerializerEditor(
        data = {
            "name": "foo",
            "procurement_price": "-1",
            "tax": "",
        }
    )
    assert serializer.is_valid() == False

def test_product_tax_is_invalid(db):
    serializer = ProductSerializerEditor(
        data = {
            "name": "foo",
            "procurement_price": "",
            "tax": "-1",
        }
    )
    assert serializer.is_valid() == False