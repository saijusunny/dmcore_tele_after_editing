# Generated by Django 4.0.2 on 2023-06-24 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0072_daily_work_target_count_daily_leeds_exists'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_leeds_exists',
            name='executive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.user_registration'),
        ),
    ]
