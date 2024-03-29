# Generated by Django 4.2.5 on 2023-12-26 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('govern', '0002_alter_news_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 12, 54, 117261)),
        ),
    ]
