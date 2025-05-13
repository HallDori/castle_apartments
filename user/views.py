# user/views.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from .forms import ProfileForm
from .models import User


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user/profile_detail.html"

    def get_context_data(self, **kwargs):
        return {"user_obj": self.request.user}


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "user/profile_form.html"
    success_url = reverse_lazy("user:profile")

    def get_object(self, queryset=None):
        # Ensure the user edits *their own* profile
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Update failed – please correct the errors.")
        return super().form_invalid(form)
from django.shortcuts import render

# Create your views here.
