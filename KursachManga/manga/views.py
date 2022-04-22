from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


posts = Titles.objects.all()


def home_page(request):
    return render(request, 'manga/main_page.html', {'post': posts})


def title_add_page(request):
    if request.method == 'POST':
        form = AddTitlesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddTitlesForm()
    return render(request, 'manga/add_title_page.html', {'form': form, 'post': posts})


def view_manga_page(request):
    return render(request, 'manga/view_manga_page.html')


def view_manga_title_page(request):
    return render(request, 'manga/view_manga_title_page.html')
