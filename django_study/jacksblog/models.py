from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import ugettext_lazy as _


class EmailUserManager(BaseUserManager):

    """Custom manager for EmailUser."""

    def _create_user(self, id, email, password, writer_name, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :param bool is_staff: whether user staff or not
        :param bool is_superuser: whether user admin or not
        :return custom_user.models.EmailUser user: user
        :raise ValueError: email is not set
        """
        now = timezone.now()
        if not id:
            raise ValueError('The given email_id must be set')
        id = self.normalize_email(id)
        user = self.model(id=id, email=email, writer_name=writer_name, create_date=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, id, email, password, writer_name, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: regular user
        """
        return self._create_user(id, email, password, writer_name, **extra_fields)

    def create_superuser(self, id, email, password, writer_name, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: admin user
        """
        return self._create_user(id, email, password, writer_name, **extra_fields)


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
    phone = models.CharField(max_length=64, null=True)
    create_date = models.DateTimeField(
        blank=True, null=True
    )

    objects = EmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:  # noqa: D101
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """Return the email."""
        return self.email

    def get_short_name(self):
        """Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


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