from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import UpdateView

from config.forms import UserForm
from .models import Profile


class ProfileDetail(PermissionRequiredMixin, DetailView):
    """Профиль пользователя"""
    permission_required = ('profiles.change_profile',)
    model = Profile
    context_object_name = "profile"
    template_name = "profiles/user-detail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = Profile.objects.get(pk=self.kwargs.get('pk')).user
        return context


class ProfileUpdate(UserPassesTestMixin, UpdateView):
    raise_exception = True
    form_class = UserForm
    model = Profile
    template_name = 'profiles/user-edit.html'
    success_url = "/"

    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] =Profile.objects.get(pk=self.kwargs.get('pk')).user
        return context
