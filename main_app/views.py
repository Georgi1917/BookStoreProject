from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main_app.forms import LogInForm, RegisterForm
from main_app.models import User


# Create your views here.


def show_initial_page(request):
    return render(request, 'html/initial.html')


def show_home_page(request):
    return render(request, 'html/index.html')


def show_about_page(request):
    return render(request, 'html/about.html')


def show_contacts_page(request):
    return render(request, 'html/contacts.html')


def show_log_in(request):
    context = {}

    form = LogInForm()
    context['form'] = form

    if request.method == "POST":
        email = request.POST["email"]

        password = request.POST["password"]

        user = User.objects.filter(email=email, password=password).first()

        if user is None:
            return redirect('initial')

        else:
            return redirect('index')

    return render(request, 'html/log-in-form.html', context)


def show_register(request):
    context = {}

    form = RegisterForm()
    context['form'] = form

    if request.method == "POST":
        form = RegisterForm(request.POST)

        try:
            form.save()
        except ValueError as ve:
            return redirect('error-page')

        return redirect('index')

    return render(request, 'html/register-form.html', context)


def error_page(request):
    return render(request, 'html/error-page.html')
