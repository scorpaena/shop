import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from product.models import Product


@pytest.fixture
def editor_group(db):
    return Group.objects.create(name="editors")


@pytest.fixture
def viewer_group(db):
    return Group.objects.create(name="viewers")


@pytest.fixture
def editor(db, editor_group):
    user = User.objects.create_user(
        username="foo",
        password="bar123$%",
    )
    user.groups.add(editor_group)
    return user


@pytest.fixture
def viewer(db, viewer_group):
    user = User.objects.create_user(
        username="foo1",
        password="bar123$%",
    )
    user.groups.add(viewer_group)
    return user


@pytest.fixture
def product(db):
    return Product.objects.create(name="name", procurement_price=1.0)


@pytest.fixture
def api_client_editor(editor):
    client = APIClient()
    client.force_authenticate(user=editor)
    return client


@pytest.fixture
def api_client_viewer(viewer):
    client = APIClient()
    client.force_authenticate(user=viewer)
    return client


@pytest.fixture
def api_client_anonymous(viewer):
    return APIClient()


def test_product_editor_list(api_client_editor, product):
    response = api_client_editor.get("/product/editor/")
    assert response.status_code == 200
    assert response.data["count"] == 1


def test_product_create(api_client_editor, product):
    response = api_client_editor.post(
        "/product/editor/",
        data={"name": "name_create", "procurement_price": 1.0},
    )
    assert response.status_code == 201
    assert Product.objects.last().name == "name_create"


def test_product_editor_retrieve(api_client_editor, product):
    response = api_client_editor.get("/product/editor/{pk}/".format(pk=product.id))
    assert response.status_code == 200
    assert response.data["name"] == product.name


def test_product_update(api_client_editor, product):
    response = api_client_editor.put(
        "/product/editor/{pk}/".format(pk=product.id),
        data={
            "name": "name_update",
            "procurement_price": 10.0,
        },
    )
    assert response.status_code == 200
    assert Product.objects.last().name == "name_update"


def test_product_destroy(api_client_editor, product):
    response = api_client_editor.delete("/product/editor/{pk}/".format(pk=product.id))
    assert response.status_code == 204
    assert Product.objects.all().count() == 0


def test_product_viewer_list(api_client_viewer, product):
    response = api_client_viewer.get("/product/viewer/")
    assert response.status_code == 200
    assert response.data["count"] == 1


def test_product_viewer_list_editor_url(api_client_viewer, product):
    response = api_client_viewer.get("/product/editor/")
    assert response.status_code == 403


def test_product_viewer_retrieve(api_client_viewer, product):
    response = api_client_viewer.get("/product/editor/{pk}/".format(pk=product.id))
    assert response.status_code == 403


def test_product_anonymous_list_editor_url(api_client_anonymous, product):
    response = api_client_anonymous.get("/product/editor/")
    assert response.status_code == 403


def test_product_anonymous_retrieve(api_client_anonymous, product):
    response = api_client_anonymous.get("/product/editor/{pk}/".format(pk=product.id))
    assert response.status_code == 403


def test_product_anonymous_list_viewer_url(api_client_anonymous, product):
    response = api_client_anonymous.get("/product/viewer/")
    assert response.status_code == 403
