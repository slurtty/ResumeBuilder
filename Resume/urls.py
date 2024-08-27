from django.conf.urls import handler403
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from Resume import views

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),
    path('profile/create', views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:profile_id>/education/create', views.EducationCreateView.as_view(), name='education-create'),

]