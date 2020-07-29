import secrets

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse

MYUSER = get_user_model()

class Stream(models.Model):
    user    = models.OneToOneField(MYUSER, on_delete=models.CASCADE)
    key     = models.CharField(max_length=20, default=secrets.token_hex(10), unique=True)
    started_on  = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()

    class Meta:
        indexes = [
            models.Index(fields=['key'])
        ]

    def __str__(self):
        return self.key

    @property
    def is_live(self):
        return self.started_on != None

    @property
    def stream_url(self):
        return reverse('stream:live_stream', args=[self.user.username])


@receiver(post_save, sender=MYUSER)
def create_new_stream(sender, instance, created, **kwargs):
    if created:
        Stream.objects.create(user=instance)
