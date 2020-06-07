# Generated by Django 3.0.7 on 2020-06-07 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0003_auto_20200607_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='commentsReply',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blogapi.Posts'),
        ),
        migrations.AddField(
            model_name='commentsreply',
            name='commentReply',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blogapi.Comments'),
        ),
    ]
