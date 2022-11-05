from django.contrib.auth import views as auth_views
from django.urls import reverse

from base.views import BaseCreateView, BaseDetailView, BaseUpdateView

from .forms import RegisterForm, UserChangeForm


class LoginView(auth_views.LoginView):
    """View to render login."""

    title = "Login"
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

    def get_success_url(self):
        return reverse("home")


class UserCreateView(BaseCreateView):
    """View to create new users."""

    title = "Register"
    template_name = "accounts/create.html"
    form_class = RegisterForm
    login_required = False
    permission_required = ()


class UserDetailView(BaseDetailView):
    """View to view user details."""

    title = "Perfil"
    template_name = "accounts/detail.html"
    login_required = True
    permission_required = ()
    context_object_name = "user"

    def get_object(self):
        return self.request.user


class UserUpdateView(BaseUpdateView):
    title = "Actualizar profile"
    form_class = UserChangeForm
    template_name = "accounts/update.html"
    login_required = True
    permission_required = ()
    context_object_name = "user"

    def get_object(self):
        return self.request.user

    def can_access(self, request):
        return self.request.user == self.get_object()
