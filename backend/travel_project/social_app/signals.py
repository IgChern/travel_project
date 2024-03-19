from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rating


@receiver(post_save, sender=Rating)
def update_post_rating(sender, instance, created, **kwargs):
    """
    Обновляет рейтинг поста при изменении рейтинга
    """
    if created:
        post = instance.post
        value = instance.value

        current_rating = post.rating

        if value == 1:
            post.rating = current_rating + 1
        elif value == -1:
            post.rating = current_rating - 1

        post.save()
