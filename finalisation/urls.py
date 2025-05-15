from django.urls import path
from .views import FinaliseWizard, FORMS
from django.views.generic import TemplateView

app_name = "finalisation"

urlpatterns = [
    path("offers/<int:pk>/finalise/",
         FinaliseWizard.as_view(FORMS), name="wizard"),
    path("offers/finalised/<int:pk>/",
         TemplateView.as_view(template_name="finalisation/done.html"),
         name="done"),
]