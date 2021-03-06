# Generated by Django 3.1.1 on 2020-10-24 07:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20201024_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_reply',
            name='title_tag',
        ),
        migrations.AddField(
            model_name='post_reply',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post_reply',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
    ]
