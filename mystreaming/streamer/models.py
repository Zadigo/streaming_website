import secrets

from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

USER = get_user_model()

class Stream(models.Model):
    user    = models.OneToOneField(USER, on_delete=models.CASCADE)
    key     = models.CharField(max_length=20, default=secrets.token_hex(10), unique=True)
    started_on  = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.key

    @property
    def is_live(self):
        return None

    @property
    def stream_url(self):
        return reverse('hls-url', args=[self.user.username])

@receiver(post_save, sender=USER)
def create_new_stream(sender, instance=None, created=False, **kwargs):
    Stream.objects.create(user=instance)