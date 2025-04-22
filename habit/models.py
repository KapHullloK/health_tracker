from django.core.exceptions import ValidationError
from django.db import models

from users.models import User

NULLABLE = {
    'blank': True,
    'null': True,
}


class Habit(models.Model):
    PERIODICITY = {
        ('day', 'Каждый день'),
        ('2 days', 'Каждые 2 дня'),
        ('3 days', 'Каждые 3 дня'),
        ('week', 'Каждую неделю'),
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habit',
                             verbose_name='user', **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='place')
    time = models.TimeField(verbose_name='time')
    action = models.CharField(max_length=255, verbose_name='action')
    pleasant = models.BooleanField(verbose_name='pleasant')
    related = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                related_name='related_habit', verbose_name='related')
    periodicity = models.CharField(max_length=30, choices=PERIODICITY, default='day',
                                   verbose_name='periodicity')
    reward = models.CharField(max_length=255, verbose_name='reward', **NULLABLE)
    lead_time = models.DurationField(verbose_name='lead time')
    is_public = models.BooleanField(default=False, verbose_name='public')

    def clean(self):
        if self.related and not self.related.pleasant:
            raise ValidationError("Можно связывать только полезные с приятными привычками")

    def __str__(self):
        return f"{self.user} - {self.action[:10]}"
