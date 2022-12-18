import uuid

from django.db import models
from django.urls import reverse

from accounts.models import User

from .enums import StatusChoices


class Session(models.Model):
    """Class that represents a Session."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="usuario",
        related_name="sesiones",
    )


    name = models.CharField(
        "nombre",
        max_length=255,
    )
    external_uuid = models.UUIDField(
        default=uuid.uuid4,
    )
    status = models.CharField(
        "estado",
        max_length=255,
        choices=StatusChoices.CHOICES,
        default=StatusChoices.CONNECTED,
    )

    def __str__(self) -> str:
        return f"Sesion: {self.name}"

    def get_absolute_url(self):
        return reverse("home")


class Notification(models.Model):
    """CLass that represents a bullying message."""

    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        verbose_name="session",
        related_name="notifications",
    )
    message = models.TextField("message")
    chat_name = models.CharField(
        "chat name",
        max_length=255,
    )
    sender = models.CharField(
        "sender",
        max_length=255,
    )
    sender_number = models.CharField(
        "sender number",
        max_length=255,
    )
    sender_name = models.CharField(
        "sender name",
        max_length=255,
    )
    date = models.DateTimeField(
        "date",
    )

    def get_absolute_url(self):
        return reverse("home")
