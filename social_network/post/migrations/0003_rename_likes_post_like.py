# Generated by Django 3.2.6 on 2021-08-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='like',
        ),
    ]
