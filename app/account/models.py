from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers.users import CustomUserManager
from uuid import uuid4


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(_("Id"), primary_key=True, editable=False, default=uuid4)
    email = models.EmailField(_("Email Address"), max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager

    def __str__(self):
        return self.email
