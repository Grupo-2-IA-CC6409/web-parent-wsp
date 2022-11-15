from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

from base.views import BaseCreateView, BaseDeleteView, BaseListView, BaseUpdateView
from parentwsp.forms import SessionChangeForm, SessionForm

from .models import Session


class SessionListView(BaseListView):
    title = "Mis sesiones"
    template_name = "parentwsp/sessions/list.html"
    login_required = True
    permission_required = ()
    model = Session

    def get_queryset(self):
        user = self.request.user
        return Session.objects.filter(user=user)


class SessionCreateView(BaseCreateView):
    title = "Crear sesion"
    template_name = "parentwsp/sessions/create.html"
    login_required = True
    permission_required = ()
    model = Session
    form_class = SessionForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["WSP_API_URL"] = settings.WSP_API_URL
        return context


class SessionUpdateView(BaseUpdateView):
    template_name = "parentwsp/sessions/update.html"
    login_required = True
    permission_required = ()
    model = Session
    form_class = SessionChangeForm

    def can_access(self, request):
        return self.object.user == request.user

    def get_title(self):
        return f"Modificar {self.object}"


class SessionDeleteView(BaseDeleteView):
    template_name = "parentwsp/sessions/delete.html"
    login_required = True
    permission_required = ()
    model = Session
    context_object_name = "session"

    def get_success_url(self) -> str:
        return reverse("home")

    def can_access(self, request):
        return self.object.user == request.user

    def get_title(self):
        return f"Borrar {self.object}"


class SessionNotificationView(BaseListView):
    template_name = "parentwsp/sessions/notify.html"
    login_required = True
    permission_required = ()
    model = Session
    form_class = SessionChangeForm

    def can_access(self, request):
        return self.object.user == request.user

    def get_title(self):
        return f"Modificar {self.object}"
