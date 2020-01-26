from django.db import models


class GymServices(models.Model):
    SERVICES_CHOICES = (
        ('GY', 'Тренажерный зал'),
        ('GP', 'Групповые программы'),
        ('SP', 'Бассейн'),
        ('MA', 'Боевые искусства'),
        ('BH', 'Банный комплекс'),
        ('BS', 'Салон красоты'),
        ('CC', 'Занятия для детей'),
        ('CS', 'Дополнительные услуги'),
    )
    name = models.CharField(
        max_length=2,
        choices=SERVICES_CHOICES,
        verbose_name='Услуги клуба')
    gym = models.ForeignKey(
        'accounts.Gym',
        on_delete=models.CASCADE,
        verbose_name='Название клуба')

    class Meta:
        verbose_name = 'Услуги клуба'
        verbose_name_plural = 'Услуги клубов'

    def __str__(self):
        return f'{self.gym.name} - {self.name}'


class GymService(models.Model):
    service = models.OneToOneField(
        'GymServices',
        on_delete=models.CASCADE,
        default='',
        verbose_name='Услуга')
    name = models.CharField(
        max_length=50,
        default='',
        verbose_name='Название услуги')
    description = models.TextField(
        verbose_name='Описание услуги',
        blank=True)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        verbose_name='Цена от')
    image = models.ImageField(
        upload_to='media/services/',
        verbose_name='Фото',
        default='media/muscules/0_i-1.jpg')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'{self.service} - {self.name}'


class TrainerService(models.Model):
    SERVICES_CHOICES = (
        ('NP', 'Индивидуальная программа питания'),
        ('TP', 'Индивидуальная программа тренировок '),
        ('CP', 'Комплексная программа(питание + тренировка)')
    )
    trainer = models.ForeignKey(
        'accounts.Trainer',
        on_delete=models.CASCADE,
        verbose_name='Тренер')
    name = models.CharField(
        max_length=2,
        choices=SERVICES_CHOICES,
        verbose_name='Услуги Тренера')
    description = models.TextField(
        verbose_name='Описание услуги',
        blank=True)
    image = models.ImageField(
        upload_to='media/services/',
        verbose_name='Фото',
        default='media/muscules/0_i-1.jpg')
    price = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        verbose_name='Цена')

    class Meta:
        verbose_name = 'Услуги тренера'
        verbose_name_plural = 'Услуги тренеров'

    def __str__(self):
        return f'{self.trainer} - {self.name}'


class OpeningHours(models.Model):
    WEEKDAYS_CHOICES = [
        (1, ('Понедельник')),
        (2, ('Вторник')),
        (3, ('Среда')),
        (4, ('Четверг')),
        (5, ('Пятница')),
        (6, ('Суббота')),
        (7, ('Воскресенье')),
    ]

    gym_service = models.ForeignKey(
        'GymService',
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='Услуга')
    weekday = models.IntegerField(
        choices=WEEKDAYS_CHOICES,
        verbose_name='День недели')
    from_hour = models.TimeField(verbose_name='Начало рабочего дня')
    to_hour = models.TimeField(verbose_name='Конец рабочего дня')

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')
        verbose_name = 'Часы работы'
        verbose_name_plural = 'Часы работы'

    def __str__(self):
        return (
            f'{self.gym_service} - {self.get_weekday_display()} \
                 - {self.from_hour}:{self.to_hour}'
            )
