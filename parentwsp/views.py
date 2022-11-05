from django.conf import settings
from django.http import HttpResponseRedirect

from base.views import BaseCreateView, BaseListView
from parentwsp.forms import SessionForm

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
