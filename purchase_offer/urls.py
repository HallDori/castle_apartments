from django.urls import path
from .views import PurchaseOfferCreateView, PurchaseOfferListView, SellerOfferList, OfferStatusUpdate

app_name = "purchase_offer"

urlpatterns = [
    path("properties/<int:pk>/offer/", PurchaseOfferCreateView.as_view(), name="create"),
    path("offers/", PurchaseOfferListView.as_view(), name="list"),
    path("seller/offers/", SellerOfferList.as_view(), name="seller_offers"),
    path("seller/offers/<int:pk>/status/", OfferStatusUpdate.as_view(), name="status_update"),
]