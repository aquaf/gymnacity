# Generated by Django 3.0.2 on 2020-01-26 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('simulators', '0001_initial'),
        ('muscules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Навание')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('execution_technique', models.TextField(blank=True, verbose_name='Техника выполнения')),
                ('image', models.ImageField(upload_to='media/exercises/', verbose_name='Изображение')),
                ('video', models.CharField(blank=True, max_length=200, verbose_name='Ссылка на видео')),
                ('auxiliary_muscles', models.ManyToManyField(blank=True, related_name='exercise_auxiliary_muscles', to='muscules.Muscule', verbose_name='Вспомогательные мышцы')),
                ('sports_equipment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='simulators.Simulator', verbose_name='Спортивный снаряд')),
                ('target_muscles', models.ManyToManyField(related_name='exercise_target_muscles', to='muscules.Muscule', verbose_name='Целевые мышцы')),
            ],
            options={
                'verbose_name': 'Упражнение',
                'verbose_name_plural': 'Упражнения',
            },
        ),
        migrations.CreateModel(
            name='ExerciseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(default=0, verbose_name='Вес')),
                ('number_of_repetitions', models.PositiveSmallIntegerField(default=0, verbose_name='Количество повторений')),
                ('number_of_approaches', models.PositiveSmallIntegerField(default=0, verbose_name='Количество подходов')),
                ('rest', models.PositiveSmallIntegerField(default=0, verbose_name='Отдых')),
                ('exercise_type', models.CharField(choices=[('Easy', 'Легкая'), ('Normal', 'Средняя'), ('Hard', 'Сложная')], default='Isolating', max_length=9, verbose_name='Тип упражнения')),
                ('difficulty', models.CharField(choices=[('Easy', 'Легкая'), ('Normal', 'Средняя'), ('Hard', 'Сложная')], default='Normal', max_length=6, verbose_name='Сложность')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Exercise', verbose_name='Упражнение')),
            ],
            options={
                'verbose_name': 'Детали упражнения',
                'verbose_name_plural': 'Детали упражнений',
            },
        ),
    ]
