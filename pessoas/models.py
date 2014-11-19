from django.db import models
from django.contrib.auth.models import AbstractUser

class Pessoa(AbstractUser):
    # username
    # firts_name
    # last_name
    # email
    # password
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined
    endereco = models.CharField(max_length=100, blank=True, null=True)
