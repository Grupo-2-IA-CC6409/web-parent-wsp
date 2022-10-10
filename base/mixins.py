# django
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseForbidden


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context

    def get_title(self):
        if self.title is None:
            msg = "You must add a title for the view"
            raise ImproperlyConfigured(msg)
        return self.title


class LoginPermissionRequiredMixin(PermissionRequiredMixin):
    """
    Verify that the user is authenticated (if required) and
    has the permission (if required)
    """

    login_required = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

    def get_login_required(self):
        if self.login_required is None:
            raise ImproperlyConfigured(
                "{0} is missing the login_required attribute. "
                "Define {0}.login_required, or override "
                "{0}.get_login_required().".format(self.__class__.__name__)
            )
        if isinstance(self.login_required, bool):
            return self.login_required
        else:
            raise ImproperlyConfigured(
                "{0} has improperly configure login_required_attribute. "
                "Define {0}.login_required as a bool or override"
                "{0}.get_login_required().".format(self.__class__.__name__)
            )

    def dispatch(self, request, *args, **kwargs):
        if self.get_login_required():
            if not request.user.is_authenticated:
                return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IndividualPermissionMixin:
    """
    Mixin that allows to force per-view permission that has access to the
    request object.
    """

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if (
            not request.user.is_anonymous
            and not request.user.is_staff
            and not self.can_access(request)
        ):
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def can_access(self, request):
        raise ImproperlyConfigured("Necessary can_access method isn't defined")
