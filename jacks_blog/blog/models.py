from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    '''
    |`writer_name`|VARCHAR(128) NOT NULL|필명|
    |`phone`|VARCHAR(64)|Mobile 번호|
    |`create_date`|DATETIME NOT NULL|등록 날짜|
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    writer_name = models.CharField(max_length=128, null= False, blank=False)
    phone = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()