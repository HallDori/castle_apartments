from django.urls import path
from .views import PurchaseOfferCreateView, PurchaseOfferListView

app_name = "purchase_offer"

urlpatterns = [
    path("properties/<int:pk>/offer/", PurchaseOfferCreateView.as_view(), name="create"),
    path("offers/", PurchaseOfferListView.as_view(), name="list"),
]