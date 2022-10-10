from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Class that represents a User"""

    email = models.EmailField(
        "email",
        unique=True,
    )
    first_name = models.CharField(
        "nombre",
        max_length=50,
    )
    last_name = models.CharField(
        "apellido",
        max_length=50,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "first_name",
        "last_name",
    )

    is_active = models.BooleanField(
        default=True,
    )
    admin = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_full_name(self):
        # Returns the full name of the user
        return f"{self.name} {self.first_last_name} {self.second_last_name}"

    def get_short_name(self):
        return f"{self.name} {self.first_last_name}"

    def __str__(self):
        return self.get_full_name()

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin

    def save(self, *args, **kwargs):
        """Normalize email address on change"""
        self.email = UserManager.normalize_email(self.email)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("profile")
