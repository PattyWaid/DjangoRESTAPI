# Generated by Django 3.0.8 on 2020-08-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0004_auto_20200814_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='is_activated',
            field=models.BooleanField(null=True),
        ),
    ]