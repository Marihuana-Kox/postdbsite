from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import PageArticles


class MainPage(View):
    '''Главная страница'''
    def get(self, request):
        template_name = 'mainapp/index.html'
        context = PageArticles.objects.get(name='home')
        return render(request, template_name, {'context': context})


class SitePageDetail(DetailView):
    '''Основные страницы сайта'''
    model = PageArticles
    template_name = 'mainapp/index.html'
    slug_field = 'name'
    context_object_name = 'context'


class ListArticleView(ListView):
    model = PageArticles
    queryset = PageArticles.objects.filter(name=0)
    template_name = 'mainapp/article_list.html'

    def get_queryset(self):
        return PageArticles.objects.filter(category=True)

