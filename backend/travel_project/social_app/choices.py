from django.db import models


class CommentVoteChoice(models.IntegerChoices):
    UPVOTE = 1
    DOWNVOTE = -1


class CommentStatus(models.TextChoices):
    PUBLISHED = "published", "Опубликован"
    DELETED = "deleted", "Удален"
