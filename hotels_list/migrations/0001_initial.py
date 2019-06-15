# Generated by Django 2.2.2 on 2019-06-11 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.TextField(max_length=50, verbose_name='Название отеля')),
                ('address', models.TextField(max_length=100, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('capacity', models.TextField(max_length=50, verbose_name='Вместимость')),
                ('type', models.TextField(max_length=50, verbose_name='Тип номера')),
                ('facilities', models.TextField(max_length=300, verbose_name='Удобства')),
                ('owner', models.TextField(max_length=50, verbose_name='Владелец отеля')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ_comment', models.CharField(default='', max_length=50, verbose_name='Тема комментария')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels_list.Hotel', verbose_name='Отель')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
