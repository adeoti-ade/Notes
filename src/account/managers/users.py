from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    This is a custom user manager which subclasses the base user manager.
    It uses email to authenticate instead of username
    """

    def create_user(self, email, password, **kwargs):
        """
        Creates and save a user with thee given email and password

        :param email:
        :param password:
        :param kwargs:
        :return user:
        """
        if not email:
            raise ValueError(_("Email must be given"))

        email = self.normalize_email(email=email)
        user = self.model(email, **kwargs)
        user.set_password(raw_password=password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and save superuser with the given email and password

        :param email:
        :param password:
        :param kwargs:
        :return user:
        """

        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        if kwargs.get("is_active") is not True:
            raise ValueError(_("Superuser must have is_active=True"))
        user = self.create_user(email=email, password=password, **kwargs)

        return user
