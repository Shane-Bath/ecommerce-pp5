# Generated by Django 3.2.21 on 2023-12-09 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_is_dealt_with'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='is_dealt_with',
            new_name='complete',
        ),
    ]
