# Generated by Django 4.2.8 on 2023-12-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_services_alter_order_options_alter_order_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='img',
            field=models.ImageField(upload_to='images/', verbose_name='Фото'),
        ),
    ]
