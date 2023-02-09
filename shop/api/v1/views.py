from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.api.v1.serializers import (
    PropertyModelSerializer, ItemModelSerializer, BasketModelSerializer,
    PriceSerializer)
from shop.models import Property, Price, Basket, Order, Brick


class PropertyListCreateAPIView(APIView):
    def get(self, request, format=None):
        property = Property.objects.all()
        serializer = PropertyModelSerializer(property, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyGetAPIView(APIView):

    def get_object(self, pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = PropertyModelSerializer(author)
        return Response(serializer.data)


class ItemCreateAPIView(APIView):
    def post(self, request):
        serializer = ItemModelSerializer(data=request.data)
        price = Price.objects.filter(property=request.data.get("property")).last()
        basket, created = Basket.objects.get_or_create(
            customer=request.user
        )
        if serializer.is_valid():
            serializer.save(price=price, basket=basket)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BasketGetAPIView(APIView):

    def get_object(self, pk):
        try:
            return Basket.objects.filter(customer=pk).last()
        except Basket.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        basket = self.get_object(pk)
        serializer = BasketModelSerializer(basket)
        return Response(serializer.data)


class PriceCreateAPIView(APIView):
    def get_object(self, pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return None

    def post(self, request, pk):
        property = self.get_object(pk)
        if property is None:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(property=property)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateAPIView(APIView):
    def post(self, request):
        order = Order.objects.create(customer=request.user)
        basket = Basket.objects.filter(customer=request.user).last()
        items = basket.item_set.all()

        for item in items:
            brick_price = item.price
            amount_brick = item.amount_brick
            property = item.property
            for _ in range(amount_brick):
                Brick.objects.create(property=property, price=brick_price, order=order)

        return Response(status=status.HTTP_200_OK)
