
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # is_active = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # is_superuser = models.BooleanField(default=False)
    ...