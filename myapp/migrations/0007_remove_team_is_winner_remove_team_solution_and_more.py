# Generated by Django 4.1.3 on 2023-07-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_code_submission_solution_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='is_winner',
        ),
        migrations.RemoveField(
            model_name='team',
            name='solution',
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.CharField(max_length=255),
        ),
    ]
