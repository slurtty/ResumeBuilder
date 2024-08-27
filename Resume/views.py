from django.shortcuts import render, get_object_or_404

from msilib.schema import ListView

from django.urls import reverse_lazy

from Resume import models, forms
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


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = models.Profile
    template_name = 'Resume/profile.html'
    form_class = forms.ProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('education-create', kwargs={'profile_id': self.object.pk})


class EducationCreateView(LoginRequiredMixin, CreateView):
    model = models.Education
    template_name = 'Resume/education.html'
    form_class = forms.EducationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(models.Profile, id=self.kwargs.get('profile_id'))
        return context

    def form_valid(self, form):
        form.instance.profile = get_object_or_404(models.Profile, id=self.kwargs.get('profile_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('education-create', kwargs={'profile_id': self.kwargs.get('profile_id')})
