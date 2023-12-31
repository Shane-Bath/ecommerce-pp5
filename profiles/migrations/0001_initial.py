# Generated by Django 3.2.21 on 2023-10-25 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('default_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=50, null=True)),
                ('default_street_address1', models.CharField(blank=True, max_length=50, null=True)),
                ('default_street_address2', models.CharField(blank=True, max_length=50, null=True)),
                ('default_county_or_state', models.CharField(blank=True, max_length=50, null=True)),
                ('default_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
