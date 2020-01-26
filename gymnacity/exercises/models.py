from django.db import models


class Exercise(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Навание')
    description = models.TextField(
        verbose_name='Описание',
        blank=True)
    execution_technique = models.TextField(
        verbose_name='Техника выполнения',
        blank=True)
    image = models.ImageField(
        upload_to='media/exercises/',
        verbose_name='Изображение')
    video = models.CharField(
        max_length=200,
        verbose_name='Ссылка на видео',
        blank=True)
    target_muscles = models.ManyToManyField(
        'muscules.Muscule',
        verbose_name='Целевые мышцы',
        related_name='exercise_target_muscles')
    auxiliary_muscles = models.ManyToManyField(
        'muscules.Muscule',
        verbose_name='Вспомогательные мышцы',
        related_name='exercise_auxiliary_muscles',
        blank=True)
    sports_equipment = models.ForeignKey(
        'simulators.Simulator',
        verbose_name='Спортивный снаряд',
        on_delete=models.PROTECT,
        blank=True)
    # comments
    # raiting

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.name


class ExerciseDetail(models.Model):
    EXERCISE_TYPE_CHOICES = (
        ('Base', 'Базовое'),
        ('Isolating', 'Изолирующее')
    )
    EXERCISE_TYPE_CHOICES = (
        ('Easy', 'Легкая'),
        ('Normal', 'Средняя'),
        ('Hard', 'Сложная')
    )
    exercise = models.ForeignKey(
        'Exercise',
        verbose_name='Упражнение',
        on_delete=models.CASCADE
    )
    weight = models.FloatField(
        default=0,
        verbose_name='Вес')
    number_of_repetitions = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество повторений')
    number_of_approaches = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество подходов')
    rest = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Отдых')
    exercise_type = models.CharField(
        max_length=9,
        choices=EXERCISE_TYPE_CHOICES,
        default='Isolating',
        verbose_name='Тип упражнения')
    difficulty = models.CharField(
        max_length=6,
        choices=EXERCISE_TYPE_CHOICES,
        default='Normal',
        verbose_name='Сложность')

    class Meta:
        verbose_name = 'Детали упражнения'
        verbose_name_plural = 'Детали упражнений'

    def __str__(self):
        return f'Вес: {self.weight} кг, \
            кол-во повторений: {self.number_of_repetitions}, \
            кол-во подходов: {self.number_of_approaches}, \
            отдых: {self.rest} мин.'
