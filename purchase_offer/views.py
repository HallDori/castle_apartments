from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView
from .forms import PurchaseOfferForm
from .models import PurchaseOffer
from property.models import Property      # import your Property model
from django.shortcuts import get_object_or_404, redirect

class PurchaseOfferCreateView(LoginRequiredMixin, CreateView):
    model         = PurchaseOffer
    form_class    = PurchaseOfferForm
    template_name = "purchase_offer/offer_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.property = get_object_or_404(Property, pk=kwargs["pk"])
        if self.property.is_sold:
            messages.error(request, "This property is already sold.")
            return redirect("property:detail", pk=self.property.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.property = self.property
        form.instance.buyer    = self.request.user
        # if a previous offer exists, replace it
        PurchaseOffer.objects.filter(property=self.property, buyer=self.request.user).delete()
        messages.success(self.request, "Your purchase offer was submitted!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("property:detail", kwargs={"pk": self.property.pk})


class PurchaseOfferListView(LoginRequiredMixin, ListView):
    template_name = "purchase_offer/offer_list.html"
    context_object_name = "offers"

    def get_queryset(self):
        return (PurchaseOffer.objects
                .select_related("property", "property__seller")
                .filter(buyer=self.request.user)
                .order_by("-created"))
from django.shortcuts import render

# Create your views here.
