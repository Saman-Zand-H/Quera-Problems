# Generated by Django 4.0.4 on 2023-03-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_alter_problem_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]