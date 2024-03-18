from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if len(password) <= 8:
            raise ValueError("Password must be more than 8 symbols")
        if email is None:
            raise TypeError("Users must have an email address.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError("Superusers must have a password.")
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(_("email"), max_length=255, unique=True, blank=True)
    username = models.CharField(_("username"), max_length=255, unique=True)
    first_name = models.CharField(_("first_name"), max_length=255, blank=True)
    last_name = models.CharField(_("last_name"), max_length=255, blank=True)
    avatar_url = models.URLField(_("photo"), blank=True)
    registration_date = models.DateTimeField(_("registration"), auto_now_add=True)
    last_login = models.DateTimeField(_("last_login"), auto_now=True)
    bio = models.TextField(_("biography"), blank=True, max_length=500)

    birthdate_year = models.IntegerField(
        _("year_of_birth"),
        validators=[MaxValueValidator(2050), MinValueValidator(1900)],
        default=1900,
        blank=True,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username", "email"]

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
