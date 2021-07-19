import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from product.models import Product

@pytest.fixture
def group(db):
    return Group.objects.create(name='editors')

@pytest.fixture
def user(db, group):
    user = User.objects.create_user(
        username = 'foo',
        password = 'bar123$%',
    )
    user.groups.add(group)
    return user

@pytest.fixture
def product(db):
    return Product.objects.create(
        name = 'name',
    )

@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


def test_product_list(api_client, product):
    response = api_client.get('/product/')
    assert response.status_code == 200
    assert response.data['count'] == 1

def test_product_create(api_client, product):
    response = api_client.post('/product/',
        data = { "name": "name_create", }
    )
    assert response.status_code == 201
    assert Product.objects.last().name == "name_create"

def test_product_retrieve(api_client, product):
    response = api_client.get('/product/{pk}/'.format(pk=product.id))
    assert response.status_code == 200
    assert response.data["name"] == product.name

def test_product_update(api_client, product):
    response = api_client.put('/product/{pk}/'.format(pk=product.id),
        data = {
        "name": "name_update", 
        "procurement_price": 10,
        }
    )
    assert response.status_code == 200
    assert Product.objects.last().name == "name_update"

def test_product_destroy(api_client, product):
    response = api_client.delete('/product/{pk}/'.format(pk=product.id))
    assert response.status_code == 204
    assert Product.objects.all().count() == 0