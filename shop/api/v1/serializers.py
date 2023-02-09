from rest_framework import serializers

from shop.models import Property, Item, Basket, Price


class PropertyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['status', 'property_type', 'name', 'amount_brick', 'description', 'amount_brick']


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['amount_brick', 'property']


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ['value']


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ['name']


class ItemSerializer(serializers.ModelSerializer):
    property = PropertySerializer()
    price = PriceSerializer()

    class Meta:
        model = Item
        fields = ['amount_brick', 'property', 'price', 'basket']


class BasketModelSerializer(serializers.ModelSerializer):
    items = ItemSerializer(source='item_set', many=True)

    class Meta:
        model = Basket
        fields = ['customer', 'items']

