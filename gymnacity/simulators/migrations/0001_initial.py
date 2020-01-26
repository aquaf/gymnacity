# Generated by Django 3.0.2 on 2020-01-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('muscules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('execution_technique', models.TextField(blank=True, verbose_name='Техника выполнения')),
                ('image', models.ImageField(upload_to='media/simulators/', verbose_name='Изображение')),
                ('video', models.CharField(blank=True, max_length=200, verbose_name='Ссылка на видео')),
                ('auxiliary_muscles', models.ManyToManyField(blank=True, related_name='simulator_auxiliary_muscles', to='muscules.Muscule', verbose_name='Вспомогательные мышцы')),
                ('target_muscles', models.ManyToManyField(related_name='simulator_target_muscles', to='muscules.Muscule', verbose_name='Целевые мышцы')),
            ],
            options={
                'verbose_name': 'Тренажер',
                'verbose_name_plural': 'Тренажеры',
            },
        ),
    ]
