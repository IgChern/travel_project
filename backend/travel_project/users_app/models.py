from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

current_year = timezone.now().year


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("Users must have a username")
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

    GENDER_OPTIONS = (
        ("f", "Женский"),
        ("m", "Мужской"),
        ("n", "Не указан"),
    )

    email = models.EmailField(_("email"), max_length=255, unique=True)
    login = models.CharField(_("username"), max_length=15, unique=True)

    first_name = models.CharField(_("first_name"), max_length=50, blank=True)
    last_name = models.CharField(_("last_name"), max_length=50, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_OPTIONS, default="n", blank=True
    )
    slug = models.SlugField(_("URL"), max_length=255, default="", blank=True)

    avatar_url = models.URLField(_("photo"), default="", blank=True)
    bio = models.TextField(_("biography"), max_length=500, blank=True)
    rating = models.FloatField(default=0, blank=True)
    registration_date = models.DateTimeField(_("registration"), auto_now_add=True)
    last_login = models.DateTimeField(_("last_login"), auto_now=True)

    comments_count = models.PositiveIntegerField(default=0)
    votes_up_count = models.PositiveIntegerField(default=0)
    votes_down_count = models.PositiveIntegerField(default=0)

    birthdate_year = models.DateField(
        _("date_of_birth"),
        validators=[MaxValueValidator(current_year), MinValueValidator(1900)],
        blank=True,
        null=True,
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["login", "email"]

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.login

    def age(self) -> int:
        if not self.birthdate_year:
            return 0
        return (timezone.now().date() - self.birthdate_year).days / 365.25
