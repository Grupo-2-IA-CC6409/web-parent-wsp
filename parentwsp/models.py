import uuid

from django.db import models
from django.urls import reverse

from accounts.models import User


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

    def __str__(self) -> str:
        return f"Sesion: {self.name}"

    def get_absolute_url(self):
        return reverse("home")


class Message(models.Model):
    """CLass that represents a bullying message."""

    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        verbose_name="session",
        related_name="messages",
    )
    message = models.CharField()
    chat = models.CharField()
    sender = models.CharField()
    sender_number = models.CharField()
