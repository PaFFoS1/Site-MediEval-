from django.shortcuts import render, redirect
from django.views import generic
from .forms import OrderForm, AddForm
from .models import Services


def order(request):
    error = ""
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма неверна"
    form = OrderForm()
    data = {
        'error': error,
        'form': form,
    }
    return render(request, 'main/order.html', data)


def home(request):
    return render(request, 'main/home.html')


def about_1(request):
    return render(request, 'main/about.html')


def faq(request):
    return render(request, 'main/FAQ.html')


class ServiceView(generic.ListView):
    template_name = 'main/services.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Services.objects.all()

def add(request):
    error = ""
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')
        else:
            error = "Форма неверна"
    form = AddForm()

    data = {
        'error': error,
        'form': form,
    }
    return render(request, 'main/add.html', data)

