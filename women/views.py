from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index(request): #Http request
    posts = Women.objects.filter(is_published=True)
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0,
               }

    return render(request, 'women/index.html', context )


def about(request): #Http request
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Войти")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {'post': post,
               'menu': menu,
               'title': post.title,
               'cat_selected': post.cat_id,
               }

    return render(request,'women/post.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat[0].id)

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts,
               'title': 'Отображение по рубкрикам',
               'cat_selected': cat[0].id
               }

    return render(request, 'women/index.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
