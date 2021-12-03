# Generated by Django 3.2.4 on 2021-07-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramclone', '0013_rename_post_likes_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
