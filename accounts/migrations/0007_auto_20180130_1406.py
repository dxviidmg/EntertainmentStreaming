# Generated by Django 2.0.1 on 2018-01-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180130_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='zone',
        ),
        migrations.AddField(
            model_name='profile',
            name='monthly_payment',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.DeleteModel(
            name='Zone',
        ),
    ]