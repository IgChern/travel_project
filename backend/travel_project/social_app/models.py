from django.db import models
from users_app.models import User
from trip_app.models import Post
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Rating(models.Model):
    """
    Модель рейтинга: Лайк - Дизлайк для постов
    """

    VOTE_CHOICES = ((1, "Like"), (-1, "Dislike"), (0, "Not Rated"))

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="ratings")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_ratings",
    )
    value = models.IntegerField(_("Value"), choices=VOTE_CHOICES)
    time_create = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        ordering = ("-time_create",)
        indexes = [models.Index(fields=["-time_create", "value"])]
        unique_together = ("post", "author")
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return self.post.title


class Comment(MPTTModel):

    STATUS_OPTIONS = (
        ("published", "Опубликовано"),
        ("deleted", "Удален"),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments_author",
        blank=True,
        null=True,
    )
    content = models.TextField(_("Comment"), max_length=3000)
    time_create = models.DateTimeField(_("Time_create"), auto_now_add=True)
    time_update = models.DateTimeField(_("Time_update"), auto_now=True)
    status = models.CharField(
        choices=STATUS_OPTIONS,
        default="published",
        max_length=10,
    )

    parent = TreeForeignKey(
        "self",
        related_name="children",
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.CASCADE,
    )

    class MTTMeta:
        """
        Сортировка по вложенности
        """

        order_insertion_by = ("-time_create",)

    class Meta:
        """
        Сортировка, название модели в админ панели
        """

        ordering = ["-time_create"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.author}:{self.content}"
