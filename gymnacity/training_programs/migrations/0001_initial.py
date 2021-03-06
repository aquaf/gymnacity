# Generated by Django 3.0.2 on 2020-01-26 09:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercises', '0001_initial'),
        ('accounts', '0001_initial'),
        ('simulators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Навание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('short_description', models.CharField(max_length=150, verbose_name='Короткое описание (до 150 символов)')),
                ('goal', models.CharField(choices=[('LW', 'Похудение'), ('MG', 'Набор мышечной массы'), ('MR', 'Сжигание жира (рельеф)'), ('PG', 'Увеличение силы'), ('ST', 'Выносливость'), ('KF', 'Поддержание формы')], default='MG', max_length=2, verbose_name='Цель')),
                ('is_paid', models.CharField(choices=[('Paid', 'Платная'), ('Free', 'Бесплатная')], default='Free', max_length=4, verbose_name='Платная/бесплатная')),
                ('price', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Стоимость')),
                ('gender', models.CharField(choices=[('Male', 'Мужчина'), ('Female', 'Женщина')], default='Male', max_length=6, verbose_name='Для кого')),
                ('difficulty', models.CharField(choices=[('Easy', 'Легкая'), ('Normal', 'Средняя'), ('Hard', 'Сложная')], default='Normal', max_length=6, verbose_name='Сложность')),
                ('place', models.CharField(choices=[('Home', 'Дома'), ('Street', 'Улица'), ('Gym', 'Тренажерный зал')], default='Gym', max_length=6, verbose_name='Место проведения')),
                ('duration', models.TimeField(blank=True, default=datetime.timedelta(seconds=3600), null=True)),
                ('training_frequency', models.IntegerField(choices=[(1, 'Один раз в неделю'), (2, 'Два раза в неделю'), (3, 'Три раза в неделю'), (4, 'Четыре раза в неделю'), (5, 'Пять раз в неделю'), (6, 'Шесть раз в неделю'), (7, 'Семь раз в неделю')], default='Gym', verbose_name='Частота тренировок')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Trainer', verbose_name='Автор программы')),
                ('exercises', models.ManyToManyField(related_name='exercises', to='exercises.Exercise', verbose_name='Упражнения')),
                ('inventory_used', models.ManyToManyField(related_name='inventory_used', to='simulators.Simulator', verbose_name='Используемый инвентарь')),
            ],
            options={
                'verbose_name': 'Программа тренировок',
                'verbose_name_plural': 'Программы тренировок',
            },
        ),
    ]
