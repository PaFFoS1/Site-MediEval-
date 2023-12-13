from django.db import models


class Order(models.Model):
    name = models.CharField('Имя заказщика', max_length=12)
    phone = models.CharField('Номер телефона', max_length=12)
    email = models.EmailField('Электронная почта', max_length=30)
    data = models.CharField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Services(models.Model):
    add = models.CharField('Наименование', max_length=12)
    img = models.ImageField('Фото', blank= False, upload_to='images/')

    def __str__(self):
        return self.add


