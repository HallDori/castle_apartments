from django.urls import path
from .views import SellerDetailView

app_name = "seller"

urlpatterns = [
    path("<int:pk>/", SellerDetailView.as_view(), name="detail"),
]
