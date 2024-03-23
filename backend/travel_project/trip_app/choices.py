from django.db import models


class PostStatus(models.TextChoices):
    DRAFT = "draft", "Черновик"
    PUBLISHED = "published", "Опубликован"
    DELETED = "deleted", "Удален"


class PostVoteChoice(models.IntegerChoices):
    UPVOTE = 1
    DOWNVOTE = -1
