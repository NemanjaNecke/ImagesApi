import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Q
from django.conf import settings


def user_directory_path(instance, filename):
    return 'profile_pic/{0}'.format(filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.get_username()


class ProfilepicManager(models.Manager):
    def create_profilepic(self, selected):
        profilepic = self.create(selected=True)
        Profilepic.objects.filter(profile=self.profile).update(
            selected=Q(pk=self.pk))
        return profilepic


class Profilepic(models.Model):

    pic = models.ImageField(
        upload_to=user_directory_path, default='profile_pic/avatar7.png', max_length=255)
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='profilepic')
    selected = models.BooleanField(default=True)

    def __str__(self):
        return self.pic.__str__()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('profile',), condition=Q(
                selected=True), name='one_selected_per_profile')
        ]

    objects = ProfilepicManager()

    @receiver(post_save, sender=Profile)
    def create_profilepic(sender, instance, created, **kwargs):
        if created:
            Profilepic.objects.create(profile=instance)

    def save(self, *args, **kwargs):
        if(Profilepic.objects.filter(selected=True)):
            Profilepic.objects.filter(profile=self.profile).update(
            selected=not Q(pk=[pk for pk in Profilepic.objects.all()]))  
        else:    
            Profilepic.objects.filter(profile=self.profile).update(
            selected=Q(pk=self.pk))
        super().save(*args, **kwargs)


@receiver(post_delete, sender=Profilepic)
def set_profilepic(sender, instance, **kwargs):
    Profilepic.objects.filter(profile=instance.profile).update(
        selected=Q(pk=Profilepic.objects.filter(profile=instance.profile).last().pk))
   


class ProfileAPIKey(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )
    apiKey = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    def __str__(self):
        return self.apiKey.__str__()

    @receiver(post_save, sender=Profile)
    def create_api_key(sender, instance, created, **kwargs):
        if created:
            ProfileAPIKey.objects.create(profile=instance)
