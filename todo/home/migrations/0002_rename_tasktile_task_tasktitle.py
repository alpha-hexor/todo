# Generated by Django 4.0.3 on 2022-03-05 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='TaskTile',
            new_name='TaskTitle',
        ),
    ]