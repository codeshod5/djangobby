from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .mangers import CustomUserManager
# from django.contrib.auth import get_user_model
# user = get_user_model()

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    # area = models.CharField(max_length=100)
    # timing = models.TimeField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserSignup(models.Model):
    email = models.EmailField(unique=True)
    area = models.CharField(max_length=100)
    timing = models.TimeField()
