from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


posts = Titles.objects.all()


def home_page(request):
    return render(request, 'manga/main_page.html', {'posts': posts})


def title_add_page(request):
    if request.method == 'POST':
        form = AddTitlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        print("dddd")
        form = AddTitlesForm()
    return render(request, 'manga/add_title_page.html', {'form': form, 'posts': posts})


def view_manga_page(request):
    return render(request, 'manga/view_manga_page.html')


def view_manga_title_page(request):
    return render(request, 'manga/view_manga_title_page.html')
