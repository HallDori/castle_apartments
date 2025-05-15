from formtools.wizard.views import SessionWizardView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from purchase_offer.models import PurchaseOffer
from .models import Finalisation
from .forms import ContactForm, PaymentForm, ReviewForm

FORMS = [("contact", ContactForm),
         ("payment", PaymentForm),
         ("review",  ReviewForm)]

TEMPLATES = {
    "contact":  "finalisation/contact_step.html",
    "payment":  "finalisation/payment_step.html",
    "review":   "finalisation/review_step.html",
}

class FinaliseWizard(SessionWizardView):
    form_list = FORMS

    # choose template based on current step
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    # --- guards ----------------------------------------------------------------
    def dispatch(self, request, *args, **kwargs):
        self.offer = get_object_or_404(
            PurchaseOffer,
            pk=kwargs["pk"],
            buyer=request.user,
            status__in=["accepted", "contingent"],
        )
        if hasattr(self.offer, "finalisation"):
            return redirect("finalisation:done", pk=self.offer.finalisation.pk)
        return super().dispatch(request, *args, **kwargs)

    # one instance carried through all steps
    def get_form_instance(self, step):
        if not hasattr(self, "_instance"):
            self._instance = Finalisation(offer=self.offer)
        return self._instance

    # put cleaned-data into Review context
    def get_context_data(self, form, **kwargs):
        ctx = super().get_context_data(form=form, **kwargs)
        if self.steps.current == "review":
            ctx["data"] = self.get_cleaned_data_for_step("contact") | \
                          self.get_cleaned_data_for_step("payment")
        return ctx

    # final save
    def done(self, form_list, **kwargs):
        fin = self.get_form_instance(None)
        fin.confirm()
        return redirect("finalisation:done", pk=fin.pk)