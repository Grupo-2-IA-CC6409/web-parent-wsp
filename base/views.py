# django
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .mixins import IndividualPermissionMixin, LoginPermissionRequiredMixin, TitleMixin


class BaseTemplateView(LoginPermissionRequiredMixin, TitleMixin, TemplateView):
    login_required = True
    permission_required = ()


class BaseDetailView(LoginPermissionRequiredMixin, TitleMixin, DetailView):
    login_required = True
    permission_required = ()


class BaseCreateView(LoginPermissionRequiredMixin, TitleMixin, CreateView):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        verbose_name = self.model._meta.verbose_name
        return f"{'Create'} {verbose_name}"


class BaseUpdateView(
    IndividualPermissionMixin, LoginPermissionRequiredMixin, TitleMixin, UpdateView
):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        return f"{'Update'} {self.object}"


class BaseListView(LoginPermissionRequiredMixin, TitleMixin, ListView):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        return self.model._meta.verbose_name_plural.title()


class BaseDeleteView(
    IndividualPermissionMixin, LoginPermissionRequiredMixin, TitleMixin, DeleteView
):
    login_required = True
    permission_required = ()

    def get_title(self):
        if self.title:
            return self.title
        verbose_name = self.model._meta.verbose_name
        return f"{'Delete'}: {verbose_name}"
