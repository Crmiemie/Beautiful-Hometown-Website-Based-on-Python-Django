# Generated by Django 4.2.5 on 2023-12-26 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('govern', '0003_news_city_alter_news_link_alter_news_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Last_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=255)),
                ('update', models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 25, 32, 24303))),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 25, 32, 23158)),
        ),
    ]
