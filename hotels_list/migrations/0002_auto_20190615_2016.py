# Generated by Django 2.2.2 on 2019-06-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='hotel',
            new_name='hotel_list',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.TextField(verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='capacity',
            field=models.TextField(verbose_name='Вместимость'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='facilities',
            field=models.TextField(verbose_name='Удобства'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel',
            field=models.TextField(verbose_name='Название отеля'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='owner',
            field=models.TextField(verbose_name='Владелец отеля'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='type',
            field=models.TextField(verbose_name='Тип номера'),
        ),
    ]
