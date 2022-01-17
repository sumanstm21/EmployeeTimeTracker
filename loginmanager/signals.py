from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import *
from django.dispatch import receiver

@receiver(post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Profile')
        instance.groups.add(group)

        Profile.objects.create(
            profile=instance,
            name=instance.username,
        )
        print('created profile')

post_save.connect(user_profile, sender=User)