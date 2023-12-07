from django.http import HttpResponse
from django.shortcuts import render

from main_app.forms import LogInForm


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

    return render(request, 'html/log-in-form.html', context)