from django.conf.urls import handler403
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from Resume import views

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),
    path('profile/create', views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:profile_id>/education/create', views.EducationCreateView.as_view(), name='education-create'),
    path('profile/<int:profile_id>/experience/create', views.ExperienceCreateView.as_view(), name='experience-create'),
    path('profile/<int:profile_id>/skills/create', views.SkillCreateView.as_view(), name='skills-create'),
    path('profile/<int:profile_id>/language/create', views.LanguageCreateView.as_view(), name='language-create'),
    path('profile/<int:profile_id>/templates/list', views.TemplatesListView.as_view(), name='templates-list'),
]

