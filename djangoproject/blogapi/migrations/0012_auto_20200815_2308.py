# Generated by Django 3.0.8 on 2020-08-15 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0011_auto_20200815_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='authorizer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogapi.PostAuthorizer'),
        ),
    ]
