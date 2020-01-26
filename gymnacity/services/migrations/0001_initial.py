# Generated by Django 3.0.2 on 2020-01-26 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('NP', 'Индивидуальная программа питания'), ('TP', 'Индивидуальная программа тренировок '), ('CP', 'Комплексная программа(питание + тренировка)')], max_length=2, verbose_name='Услуги Тренера')),
                ('description', models.TextField(blank=True, verbose_name='Описание услуги')),
                ('image', models.ImageField(default='media/muscules/0_i-1.jpg', upload_to='media/services/', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Цена')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Trainer', verbose_name='Тренер')),
            ],
            options={
                'verbose_name': 'Услуги тренера',
                'verbose_name_plural': 'Услуги тренеров',
            },
        ),
        migrations.CreateModel(
            name='GymServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('GY', 'Тренажерный зал'), ('GP', 'Групповые программы'), ('SP', 'Бассейн'), ('MA', 'Боевые искусства'), ('BH', 'Банный комплекс'), ('BS', 'Салон красоты'), ('CC', 'Занятия для детей'), ('CS', 'Дополнительные услуги')], max_length=2, verbose_name='Услуги клуба')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Gym', verbose_name='Название клуба')),
            ],
            options={
                'verbose_name': 'Услуги клуба',
                'verbose_name_plural': 'Услуги клубов',
            },
        ),
        migrations.CreateModel(
            name='GymService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Название услуги')),
                ('description', models.TextField(blank=True, verbose_name='Описание услуги')),
                ('price', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Цена от')),
                ('image', models.ImageField(default='media/muscules/0_i-1.jpg', upload_to='media/services/', verbose_name='Фото')),
                ('service', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='services.GymServices', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], verbose_name='День недели')),
                ('from_hour', models.TimeField(verbose_name='Начало рабочего дня')),
                ('to_hour', models.TimeField(verbose_name='Конец рабочего дня')),
                ('gym_service', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='services.GymService', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Часы работы',
                'verbose_name_plural': 'Часы работы',
                'ordering': ('weekday', 'from_hour'),
                'unique_together': {('weekday', 'from_hour', 'to_hour')},
            },
        ),
    ]
