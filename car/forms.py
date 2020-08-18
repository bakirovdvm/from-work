from django import forms
from django.forms import TextInput
from django.forms import ModelForm
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name_auto', 'model_auto', 'year', 'color', 'length', 'width', 'height', 'clearance', 'engine_capacity', 'transmission']
        #exclude = ['']
        widgets = {
            'name_auto': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите марку автомобиля',
            }),
            'model_auto': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите модель автомобиля',
            }),
            'year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите год выпуска автомобиля',
            }),
            'engine_capacity': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите объем двигателя',
            }),
            'transmission': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тип коробки переключения передач',
            }),
            'color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цвет автомобиля',
            }),
            'length': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите длину автомобиля',
            }),
            'width': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ширину автомобиля',
            }),
            'height': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите высоту автомобиля',
            }),
            'clearance': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите клиренс автомобиля',
            }),

        }


