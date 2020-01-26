from django.db import models


class Muscule(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(
        upload_to='media/muscules/',
        verbose_name='Картинка',
        blank=True)

    class Meta:
        verbose_name = 'Мышца'
        verbose_name_plural = 'Мышцы'

    def __str__(self):
        return self.name
