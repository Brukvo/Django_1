from django.db import models
from django.contrib.auth.models import AbstractUser

class CommonUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
    name = models.CharField(verbose_name='имя', max_length=32)
    bio = models.TextField(verbose_name='о себе', blank=True)

    def __str__(self):
        return self.name
