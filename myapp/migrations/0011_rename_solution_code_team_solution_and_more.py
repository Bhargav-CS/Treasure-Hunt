# Generated by Django 4.1.3 on 2023-07-25 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_team_is_winner_team_solution_code_alter_team_members_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='solution_code',
            new_name='solution',
        ),
        migrations.AddField(
            model_name='team',
            name='submission_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]