# Generated by Django 4.2.5 on 2023-10-19 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthApp', '0006_rename_description_treatment_possible_diseases_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='possible_diseases',
        ),
    ]
