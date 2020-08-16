# Generated by Django 3.0.8 on 2020-08-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='email',
            field=models.EmailField(default='EMAIl NOT PROVIDED', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.CharField(max_length=20),
        ),
    ]