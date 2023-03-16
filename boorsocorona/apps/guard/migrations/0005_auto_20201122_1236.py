# Generated by Django 3.1.3 on 2020-11-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guard', '0004_remove_blockedip_url_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockedip',
            name='key',
        ),
        migrations.AlterField(
            model_name='blockedip',
            name='ban_time',
            field=models.PositiveIntegerField(default=360),
        ),
    ]
