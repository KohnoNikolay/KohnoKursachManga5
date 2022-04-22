from django.urls import path

from .views import *

'''Изменить путь path в "", "add/" на указанный во views.py.'''
urlpatterns = [
    path('', home_page, name='home'),
    path('add/', title_add_page, name='title_add_page'),  # Переход на страницу добавления тайтла.
    path('view_manga_page/', view_manga_page, name='view_manga_page'),  # Переход на страницу просмотра манги.
    path('view_manga_title_page/', view_manga_title_page, name='view_manga_title_page'),  # Переход на страницу визитку тайтла.
]

# path('<slug:slug>/', admin.site.urls, name='Title_page'),
# Переход на страницу визитку тайтла. Адрес страницы изменяем по slug тайтла.

# path('<slug_title:slug>/<slug_chapter:slug>/', admin.site.urls, name='Title_chapter_view'),
# Переход на страницу просмотра тайтла. Адрес обязан включать в себя название тайтла и номер главы.