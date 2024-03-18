from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = PasswordResetTokenGenerator().make_token(instance)
        token, _ = Token.objects.get_or_create(user=instance)
