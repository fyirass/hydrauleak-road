# Generated by Django 4.0.4 on 2022-11-25 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_intervention_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Maps',
            new_name='Map',
        ),
        migrations.RenameModel(
            old_name='Pipes',
            new_name='Pipe',
        ),
    ]