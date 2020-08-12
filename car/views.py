from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car
from .forms import CarForm

# def car(request):
#     return HttpResponse('allo')

def home(request):
    return render(request, ('car/home.html'))


def car(request):
    cars = Car.objects.all()
    form = CarForm(request.POST or None)
    success = 'Поздравляю! вы добавили автомобиль!'
    if request.method == 'POST':
        #print(request.POST) - Проверка отправки данных в терминале
        form = CarForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('car_table')

    return render(request, ('car/car_list.html'), {'cars': cars, 'form': form, 'success': success})


def car_table(request):
    cars = Car.objects.all()
    return render(request, ('car/car_table.html'), {'cars': cars})
