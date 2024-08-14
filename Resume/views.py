from django.shortcuts import render

from Resume import models
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileListView(LoginRequiredMixin, ListView):
    model = models.Profile
    context_object_name = 'profile'
    template_name = 'resume/profile.html'

    def get_queryset(self):
        queryset = super(ProfileListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

