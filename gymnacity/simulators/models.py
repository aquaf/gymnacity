from django.db import models


class Simulator(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название')
    description = models.TextField(
        blank=True,
        verbose_name='Описание')
    execution_technique = models.TextField(
        verbose_name='Техника выполнения',
        blank=True)
    image = models.ImageField(
        upload_to='media/simulators/',
        verbose_name='Изображение')
    video = models.CharField(
        max_length=200,
        verbose_name='Ссылка на видео',
        blank=True)
    target_muscles = models.ManyToManyField(
        'muscules.Muscule',
        verbose_name='Целевые мышцы',
        related_name='simulator_target_muscles')
    auxiliary_muscles = models.ManyToManyField(
        'muscules.Muscule',
        verbose_name='Вспомогательные мышцы',
        related_name='simulator_auxiliary_muscles',
        blank=True)
    # comments
    # raiting

    class Meta:
        verbose_name = 'Тренажер'
        verbose_name_plural = 'Тренажеры'

    def __str__(self):
        return self.name
