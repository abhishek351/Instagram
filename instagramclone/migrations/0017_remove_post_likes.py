# Generated by Django 3.2.4 on 2021-09-03 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagramclone', '0016_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
