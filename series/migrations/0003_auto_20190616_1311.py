# Generated by Django 2.0.1 on 2019-06-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_auto_20190616_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(),
        ),
    ]
