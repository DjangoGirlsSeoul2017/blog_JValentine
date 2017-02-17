from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import EmailUserChangeForm, EmailUserCreationForm
from .models import BlogEmailUser

# Register your models here.

class BlogEmailUserAdmin(EmailUserAdmin):
    """EmailUser Admin model."""

    """
    Create and save an EmailUser with the given email and password.
    :param str id: user id(email)
    :param str password: user password
    :param str writer_name: user writer_name
    :param str email: user email
    :param str phone: user phone
    :param str create_date: user create_date
    :param str lastlogin_date: user lastlogin_date
    :return custom_user.models.BlogEmailUser user: user
    """

    fieldsets = (
        (None, {'fields': ('id', 'password', 'writer_name', 'email', 'phone')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
                         None, {
                             'classes': ('wide',),
                             'fields': ('email', 'password1', 'password2')
                         }
                     ),
    )

    # The forms to add and change user instances
    form = EmailUserChangeForm
    add_form = EmailUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Register your models here.
admin.site.register(BlogEmailUser, BlogEmailUserAdmin)