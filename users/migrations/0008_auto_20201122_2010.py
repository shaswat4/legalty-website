# Generated by Django 3.1.1 on 2020-11-22 14:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201122_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lawyerprofile',
            options={'ordering': ('-date_added',)},
        ),
        migrations.AddField(
            model_name='lawyerprofile',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
