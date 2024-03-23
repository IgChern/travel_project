from typing import Iterable
from django.db import models
from users_app.models import User
from django.utils.translation import gettext_lazy as _
from .choices import PostStatus, PostVoteChoice
from users_app.models import User
from django.db.models import UniqueConstraint
from django.utils.text import slugify


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_trip")
    title = models.CharField(_("Title"), max_length=255, blank=True)
    location = models.CharField(_("Location"), max_length=255)
    description = models.TextField(_("Description"), blank=True)
    slug = models.SlugField(_("URL"), max_length=255, default="", blank=True)
    start_date = models.DateTimeField(_("Start_date"))
    end_date = models.DateTimeField(_("End_date"))
    photo = models.URLField(_("Photo"), blank=True)

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self) -> str:
        return self.location

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, related_name="author_posts", default=1
    )
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE, related_name="user_trip")
    title = models.CharField(_("Название поста"), max_length=255)

    slug = models.SlugField(_("URL"), max_length=255, default="", blank=True)
    status = models.CharField(
        _("status"), choices=PostStatus.choices, default="published", max_length=10
    )
    rating = models.FloatField(default=0, blank=True)
    description = models.TextField(_("Description"), blank=True)
    photo = models.URLField(_("Photo"), blank=True)

    comments_count = models.PositiveIntegerField(default=0)
    votes_up_count = models.PositiveIntegerField(default=0)
    votes_down_count = models.PositiveIntegerField(default=0)
    rating = models.IntegerField(default=0)

    create = models.DateTimeField(_("Date_create"), auto_now_add=True)
    update = models.DateTimeField(_("Date_update"), auto_now=True)

    objects = models.Manager()
    custom = PostManager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PostRating(models.Model):
    """Model to store post votes."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_votes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="votes")
    value = models.SmallIntegerField(choices=PostVoteChoice.choices, db_index=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=("user", "post"), name="user_post_vote"),
        ]
        indexes = [
            models.Index(fields=["post", "user", "value"]),
        ]

    def __str__(self):
        return f"{self.post}: {self.value}"
