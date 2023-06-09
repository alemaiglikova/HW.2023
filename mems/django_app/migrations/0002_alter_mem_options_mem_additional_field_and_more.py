# Generated by Django 4.2.3 on 2023-07-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mem',
            options={'ordering': ('-date_time', 'title'), 'verbose_name': 'Мем', 'verbose_name_plural': 'Мемы'},
        ),
        migrations.AddField(
            model_name='mem',
            name='additional_field',
            field=models.CharField(blank=True, max_length=100, verbose_name='Дополнительное поле'),
        ),
        migrations.AddField(
            model_name='mem',
            name='recent_user',
            field=models.BooleanField(default=False, verbose_name='Недавний пользователь'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Наименование'),
        ),
    ]
