# Generated by Django 3.1.1 on 2020-10-23 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',)},
        ),
    ]
