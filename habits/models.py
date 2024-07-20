from django.db import models

from datetime import timedelta
from config import settings


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Создатель привычки',
        help_text='Укажите создателя привычки',
        **NULLABLE,
    )
    place = models.CharField(
        max_length=100,
        verbose_name='Место выполнения привычки',
        help_text='Укажите место выполнения привычки',
        **NULLABLE,
    )
    time = models.DateTimeField(
        verbose_name='Дата и время выполнения привычки',
        help_text='Укажите дату и время выполнения привычки',
        **NULLABLE,
    )
    action = models.CharField(
        max_length=200,
        verbose_name='Действие, которое требуется сделать',
        help_text='Укажите действие, которое требуется сделать',
        **NULLABLE,
    )
    pleasant_habit_sign = models.BooleanField(
        verbose_name='Признок приятной привычки',
        help_text='Укажите, является ли привычка приятной',
        default=False,
        **NULLABLE,
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Связанная привычка',
        help_text='Укажите связанную привычку',
        **NULLABLE
    )
    periodicity = models.SmallIntegerField(
        default=1,
        verbose_name='Периодичность выполнения привычки',
        help_text='Укажите периодичность от 1 до 7,'
        'где 1 - один раз в неделю, а 7 - это каждый день.',
        **NULLABLE,
    )
    reward = models.CharField(
        max_length=200,
        verbose_name='Награда за выполнение привычки',
        help_text='Укажите награду за выполнение привычки',
        **NULLABLE,
    )
    duration = models.DurationField(
        verbose_name='Продолжительность выполнения привычки',
        help_text='Укажите продолжительность выполнения привычки',
        default=timedelta(seconds=120),
        **NULLABLE,
    )
    is_published = models.BooleanField(
        verbose_name='Признак публичности',
        help_text='Укажите, опубликована ли привычка',
        default=True,
        **NULLABLE,
    )

    def __str__(self):
        return f'{self.owner} будет {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
