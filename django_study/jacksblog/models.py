from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

user = get_user_model().objects.get(email="jackvalentine@jackarchive.com")


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):

    """
    Create and save an EmailUser with the given email and password.
    :param str id: user id_email
    :param str password: user password
    :param str writer_name: user writer_name
    :param str email: user email
    :param str phone: user phone
    :param str create_date: user create_date
    :param str lastlogin_date: user lastlogin_date
    :return custom_user.models.BlogEmailUser user: user
    :raise ValueError: email is not set
    """
    id = models.CharField(max_length=128)
    password = models.CharField(max_length=512)
    writer_name = models.CharField(max_length=128)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=64)
    create_date = models.DateTimeField(
        blank=True, null=True
    )


class BlogEmailUser(AbstractBaseUser, PermissionsMixin):
    """
   Concrete class of AbstractEmailUser.
   Use this if you don't need to extend EmailUser.
   """
    class Meta(AbstractEmailUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Post(models.Model):
    id = models.ForeignKey('auth.User')
    title = models.CharField(max_length=1024)
    text = models.TextField()
    publish = models.CharField(max_length=1)
    created_date = models.DateTimeField(
        blank=True, null=True
    )