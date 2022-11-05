import uuid

from django.db import models

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
