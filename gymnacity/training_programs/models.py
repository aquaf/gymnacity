from django.db import models
from datetime import timedelta


class TrainingProgram(models.Model):
    GOAL_CHOICES = (
        ('LW', 'Похудение'),
        ('MG', 'Набор мышечной массы'),
        ('MR', 'Сжигание жира (рельеф)'),
        ('PG', 'Увеличение силы'),
        ('ST', 'Выносливость'),
        ('KF', 'Поддержание формы')
    )
    PAID_CHOICES = (
        ('Paid', 'Платная'),
        ('Free', 'Бесплатная')
    )
    GENDER_CHOICES = (
        ('Male', 'Мужчина'),
        ('Female', 'Женщина')
    )
    PROGRAM_TYPE_CHOICES = (
        ('Easy', 'Легкая'),
        ('Normal', 'Средняя'),
        ('Hard', 'Сложная')
    )
    PLACE_CHOICES = (
        ('Home', 'Дома'),
        ('Street', 'Улица'),
        ('Gym', 'Тренажерный зал'),
    )
    FREQUENCY_CHOICES = (
        (1, ('Один раз в неделю')),
        (2, ('Два раза в неделю')),
        (3, ('Три раза в неделю')),
        (4, ('Четыре раза в неделю')),
        (5, ('Пять раз в неделю')),
        (6, ('Шесть раз в неделю')),
        (7, ('Семь раз в неделю')),
    )
    name = models.CharField(max_length=100, verbose_name='Навание')
    description = models.TextField(verbose_name='Описание')
    short_description = models.CharField(
        max_length=150,
        verbose_name='Короткое описание (до 150 символов)')
    author = models.ForeignKey(
        'accounts.Trainer',
        on_delete=models.CASCADE,
        verbose_name='Автор программы')
    goal = models.CharField(
        max_length=2,
        choices=GOAL_CHOICES,
        default='MG',
        verbose_name='Цель')
    is_paid = models.CharField(
        max_length=4,
        choices=PAID_CHOICES,
        default='Free',
        verbose_name='Платная/бесплатная')
    price = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        verbose_name='Стоимость')
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default='Male',
        verbose_name='Для кого')
    difficulty = models.CharField(
        max_length=6,
        choices=PROGRAM_TYPE_CHOICES,
        default='Normal',
        verbose_name='Сложность')
    place = models.CharField(
        max_length=6,
        choices=PLACE_CHOICES,
        default='Gym',
        verbose_name='Место проведения')
    duration = models.TimeField(
        null=True,
        blank=True,
        default=timedelta(hours=1))
    training_frequency = models.IntegerField(
        choices=FREQUENCY_CHOICES,
        default='Gym',
        verbose_name='Частота тренировок')
    inventory_used = models.ManyToManyField(
        'simulators.Simulator',
        related_name='inventory_used',
        verbose_name='Используемый инвентарь')
    exercises = models.ManyToManyField(
        'exercises.Exercise',
        related_name='exercises',
        verbose_name='Упражнения')
    # comments
    # reiting

    class Meta:
        verbose_name = 'Программа тренировок'
        verbose_name_plural = 'Программы тренировок'

    def __str__(self):
        return self.name
