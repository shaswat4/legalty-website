# Generated by Django 3.1.1 on 2020-11-22 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201122_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lawyerprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='lawyerprofile',
            name='date_added',
        ),
    ]
