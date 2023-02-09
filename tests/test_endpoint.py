import pytest

from rest_framework.test import APIClient

from shop.models import Property

client = APIClient()


@pytest.mark.django_db
def test_create_price():
    property = Property.objects.create(
        status="developing",
        property_type="building",
        name="Edificio A",
        amount_brick=10,
        description="un edificio en zapopan"
    )

    expected_json = {
        "value": 300
    }

    response = client.post(
        f"/shop/api/v1/property/{property.id}/price", data=expected_json, format="json"
    )

    data = response.data

    assert response.status_code == 201
    assert isinstance(response.data, dict)
    assert isinstance(data["value"], int)
    assert data["value"] == expected_json['value']


@pytest.mark.django_db
def test_create_property():
    expected_json = {
        "status": "finished",
        "property_type": "building",
        "name": "Edificio A",
        "amount_brick": 200,
        "description": "Un edificio muy chingon"
    }

    response = client.post(f"/shop/api/v1/properties/", data=expected_json, format="json")

    assert response.status_code == 201
    assert isinstance(response.data, dict)


@pytest.mark.django_db
def test_get_property():

    response = client.get(f"/shop/api/v1/properties/")

    assert response.status_code == 200
    assert isinstance(response.data, list)
