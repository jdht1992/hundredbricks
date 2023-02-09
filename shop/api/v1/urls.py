from django.urls import path

from shop.api.v1.views import (
    PropertyListCreateAPIView, ItemCreateAPIView, BasketGetAPIView,
    PriceCreateAPIView, OrderCreateAPIView
)

urlpatterns = [
    path("api/v1/properties/", PropertyListCreateAPIView.as_view()),
    path("api/v1/basket/", ItemCreateAPIView.as_view()),
    path("api/v1/checkout/<int:pk>/", BasketGetAPIView.as_view()),
    path("api/v1/property/<int:pk>/price", PriceCreateAPIView.as_view()),
    path("api/v1/order/", OrderCreateAPIView.as_view()),
]
