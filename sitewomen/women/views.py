from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавьте статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулиа Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
    ]

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'woman/index.html', context=data)

def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'woman/about.html', data)

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def login(request):
    return HttpResponse("Авторизация")

def contact(request):
    return HttpResponse("Обратная связь")

def addpage(request):
    return HttpResponse("добавление статьи")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2023:
        #raise Http404()
        uri = reverse('cats', args=('music',))
        return HttpResponseRedirect(uri)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    #return HttpResponseNotFound("<h1>Страница не найдена</h1>")
    data = {'title': 'Страница не найдена - 404',
            'menu': menu,
    }
    return render(request, 'woman/404.html', data)