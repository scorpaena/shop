import pytest
from decimal import Decimal
from product.models import Product
from adjustment.models import Adjustment
from constance import config


@pytest.fixture
def adjustment(db):
    return Adjustment.objects.create(
        procurement_price_lower_limit=0.0,
        procurement_price_upper_limit=0.5,
        extra_charge=25,
        risk=25,
    )


@pytest.fixture
def adjustment1(db):
    return Adjustment.objects.create(
        procurement_price_lower_limit=0.5,
        procurement_price_upper_limit=1.0,
        extra_charge=1,
        risk=1,
    )


def test_product_with_own_values(db, adjustment, adjustment1):
    product = Product.objects.create(
        name="product", procurement_price=0.5, tax=10, extra_charge=5, risk=5
    )
    price = product.sticker_price
    proc_price = product.procurement_price
    charge = product.extra_charge
    tax = product.tax
    risk = product.risk
    sum_charge = charge + tax + risk
    assert price == round(Decimal(proc_price * (1 + sum_charge / 100)), 1)


def test_product_with_adjustment_values(db, adjustment, adjustment1):
    product = Product.objects.create(
        name="product",
        procurement_price=0.5,
        tax=10,
    )
    price = product.sticker_price
    proc_price = product.procurement_price
    tax = product.tax
    charge = adjustment.extra_charge
    risk = adjustment.risk
    sum_charge = charge + tax + risk
    assert price == round(Decimal(proc_price * (1 + sum_charge / 100)), 1)


def test_product_with_adjustment1_values(db, adjustment, adjustment1):
    product = Product.objects.create(
        name="product",
        procurement_price=0.6,
        tax=10,
    )
    price = product.sticker_price
    proc_price = product.procurement_price
    tax = product.tax
    charge = adjustment1.extra_charge
    risk = adjustment1.risk
    sum_charge = charge + tax + risk
    assert price == round(Decimal(proc_price * (1 + sum_charge / 100)), 1)


def test_product_with_constance_values(db, adjustment, adjustment1):
    adjustment.delete()
    product = Product.objects.create(
        name="product",
        procurement_price=0.5,
    )
    price = product.sticker_price
    proc_price = product.procurement_price
    tax = config.TAX
    charge = config.EXTRA_CHARGE
    risk = config.RISK
    sum_charge = charge + tax + risk
    assert price == round(Decimal(proc_price * (1 + sum_charge / 100)), 1)
