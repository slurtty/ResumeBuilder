from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy

from Resume import models, forms
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseCreateView(LoginRequiredMixin, CreateView):
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


class ProfileListView(LoginRequiredMixin, ListView):
    model = models.Profile
    context_object_name = 'profiles'
    template_name = 'resume/my_profiles.html'

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


class EducationCreateView(BaseCreateView):
    model = models.Education
    template_name = 'Resume/education.html'
    form_class = forms.EducationForm

    def get_success_url(self):
        return reverse_lazy('education-create', kwargs={'profile_id': self.kwargs.get('profile_id')})


class ExperienceCreateView(BaseCreateView):
    model = models.Experience
    template_name = 'Resume/experience.html'
    form_class = forms.ExperienceForm

    def get_success_url(self):
        return reverse_lazy('experience-create', kwargs={'profile_id': self.kwargs.get('profile_id')})


class SkillCreateView(BaseCreateView):
    model = models.Skill
    template_name = 'Resume/skills.html'
    form_class = forms.SkillForm

    def get_success_url(self):
        return reverse_lazy('skills-create', kwargs={'profile_id': self.kwargs.get('profile_id')})


class LanguageCreateView(BaseCreateView):
    model = models.Language
    template_name = 'Resume/language.html'
    form_class = forms.LanguageForm

    def get_success_url(self):
        return reverse_lazy('language-create', kwargs={'profile_id': self.kwargs.get('profile_id')})


class TemplatesListView(LoginRequiredMixin, ListView):
    model = models.ResumeTemplate
    template_name = "Resume/templates.html"
    context_object_name = "templates"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(models.Profile, id=self.kwargs.get('profile_id'))
        return context


class ResumeDetailView(LoginRequiredMixin, DetailView):
    model = models.ResumeTemplate
    context_object_name = 'template'

    def get_template_names(self):
        template = get_object_or_404(models.ResumeTemplate, pk=self.kwargs['pk'])
        return ['Resume/' + template.template]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(models.Profile, id=self.kwargs.get('profile_id'))
        return context






