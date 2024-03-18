from django.db import models
from users_app.models import User
from trip_app.models import Post
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Rating(models.Model):
    """
    Модель рейтинга: Лайк - Дизлайк для постов
    """

    VOTE_CHOICES = ((1, "Like"), (2, "Dislike"))

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    value = models.IntegerField(_("Value"), choices=VOTE_CHOICES)
    time_create = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        ordering = ("-time_create",)
        indexes = [models.Index(fields=["-time_create", "value"])]
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return self.post.place_name
