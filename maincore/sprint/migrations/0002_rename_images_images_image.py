# Generated by Django 4.2.11 on 2024-04-18 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='image',
        ),
    ]