# Generated by Django 4.0.2 on 2023-06-24 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0070_lead_delay_sub_target'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead_delay',
            old_name='end_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='lead_delay',
            name='start_date',
        ),
    ]
