from django.forms import ModelForm, TextInput, EmailInput, FileInput
from .models import Order, Services


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'data']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя заказщика'
            }),
            "phone": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Номер телефона"
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта'
            }),
            "data": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Желаемая дата реализации'
            })
        }

class AddForm(ModelForm):
    class Meta:
        model = Services
        fields = ['add', 'img']

        widgets = {
            "add": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            "img": FileInput(attrs={
                'class': "form-control",
                'type': "file"
            })
        }