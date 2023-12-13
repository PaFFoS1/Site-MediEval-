# Generated by Django 4.2.8 on 2023-12-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='Имя заказщика')),
                ('surname', models.CharField(max_length=12, verbose_name='Фамилия заказщика')),
                ('middle_name', models.CharField(max_length=12, verbose_name='Отчество заказщика')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=30, verbose_name='Электронная почта')),
                ('data', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]