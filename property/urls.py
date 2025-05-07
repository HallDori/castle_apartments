from django.urls import path
from .views import PropertyListView, PropertyDetailView

app_name = "property"

urlpatterns = [
    path("", PropertyListView.as_view(), name="list"),          # /  -> catalogue
    path("<int:pk>/", PropertyDetailView.as_view(), name="detail"),  # /5/ -> detail
]
