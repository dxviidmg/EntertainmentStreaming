# Generated by Django 2.0.1 on 2018-01-21 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TV', '0005_auto_20180120_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='logo',
            new_name='image',
        ),
    ]