# Generated by Django 4.2.5 on 2023-12-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='belongs_to',
            field=models.CharField(max_length=255),
        ),
    ]
