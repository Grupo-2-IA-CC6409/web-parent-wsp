import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from base.views import BaseCreateView, BaseDeleteView, BaseListView, BaseUpdateView
from parentwsp.forms import SessionChangeForm, SessionForm

from .enums import StatusChoices
from .models import Notification, Session
from .serializers import NotificationSerializer


class SessionListView(BaseListView):
    title = "Mis sesiones"
    template_name = "parentwsp/sessions/list.html"
    login_required = True
    permission_required = ()
    model = Session

    def get_queryset(self):

        user = self.request.user
        return Session.objects.filter(user=user).order_by("status")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["statusChoices"] = StatusChoices
        return context


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
    template_name = "parentwsp/sessions/notification.html"
    login_required = True
    permission_required = ()
    model = Notification

    def get_queryset(self):
        session_pk = self.kwargs.get("pk")
        return Notification.objects.filter(session_id=session_pk)

    def can_access(self, request):
        session_pk = self.kwargs.get("pk")
        return Session.objects.get(pk=session_pk).user == request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_pk = self.kwargs.get("pk")
        context["session"] = Session.objects.get(pk=session_pk)
        context["statusChoices"] = StatusChoices
        return context

    def get_title(self):
        session_pk = self.kwargs.get("pk")
        session = Session.objects.get(pk=session_pk)
        return f"Notificaciones de {session}"


class SessionNotificationAPI(APIView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        data = {
            "session": Session.objects.get(
                external_uuid=request.data.get("session")
            ).pk,
            "message": request.data.get("message"),
            "chat_name": request.data.get("chat_name"),
            "sender": request.data.get("sender"),
            "sender_number": request.data.get("sender_number"),
            "sender_name": request.data.get("sender_name"),
            "date": datetime.utcfromtimestamp(int(request.data.get("date"))).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

        # create email
        email_address = "wsp.parental@gmail.com"
        email_password = "fxvaeakhwfokkuch"
        ctx = ssl.create_default_context()
        msg = EmailMessage()
        msg["Subject"] = "Notificación"
        msg["From"] = email_address
        msg["To"] = Session.objects.get(
            external_uuid=request.data.get("session")
        ).user.email
        msg.set_content("Se ha identificado un mensaje de odio")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        serializer = NotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionDisconnectAPI(APIView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        session = Session.objects.get(external_uuid=request.data.get("session"))
        session.status = StatusChoices.DISCONNECTED
        session.save()

        return Response(status=status.HTTP_200_OK)
