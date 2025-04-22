from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class User(AbstractUser):
    tg_chat_id = models.CharField(max_length=100, **NULLABLE, verbose_name='tg chat id')

    def __str__(self):
        return self.username
