# Generated by Django 3.2.21 on 2023-10-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catergory',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
