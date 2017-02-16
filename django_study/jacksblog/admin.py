from django.contrib import admin
from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import BlogEmailUser

# Register your models here.

class BlogEmailUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """
    pass

# Register your models here.
admin.site.register(BlogEmailUser, BlogEmailUserAdmin)