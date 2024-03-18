from django.db import models
from users_app.models import User
from django.utils.translation import gettext_lazy as _


class PostManager(models.Manager):
    """
    Кастомный менеджер для модели постов
    """

    def all(self):
        """
        Список постов (SQL запрос с фильтрацией по статусу опубликованно для автора)
        """
        return self.get_queryset().select_related("author").filter(status="published")


# Create your models here.
class Trips(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_trip"
    )
    location = models.CharField(_("Location"), max_length=255)
    title = models.CharField(_("Title"), max_length=255, blank=True)
    description = models.TextField(_("Description"), blank=True)
    start_date = models.DateTimeField(_("Start_date"))
    end_date = models.DateTimeField(_("End_date"))
    photo = models.URLField(_("Photo"), blank=True)

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self) -> str:
        return self.title


class Post(models.Model):

    STATUS_OPTIONS = (("published", "Опубликовано"), ("draft", "Черновик"))

    author = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, related_name="author_posts", default=1
    )
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE, related_name="user_trip")
    slug = models.SlugField(_("URL"), max_length=255, blank=True)
    status = models.CharField(
        _("status"), choices=STATUS_OPTIONS, default="published", max_length=10
    )
    place_name = models.CharField(_("Place_name"), max_length=255)
    place_type = models.CharField(_("Place_type"), max_length=255, blank=True)
    description = models.TextField(_("Description"), blank=True)
    photo = models.URLField(_("Photo"), blank=True)

    create = models.DateTimeField(_("Date_create"), auto_now_add=True)
    update = models.DateTimeField(_("Date_update"), auto_now=True)

    objects = models.Manager()
    custom = PostManager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return self.place_name
