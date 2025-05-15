from django.views.generic import DetailView
from .models import Seller

class SellerDetailView(DetailView):
    model = Seller
    template_name = "seller/seller_detail.html"