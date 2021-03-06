# Generated by Django 3.0.2 on 2020-01-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muscule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='media/muscules/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Мышца',
                'verbose_name_plural': 'Мышцы',
            },
        ),
    ]
