from django.conf.urls import handler403
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from Resume import views

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),

]