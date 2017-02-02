# -*- coding: utf-8 -*-

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, Comment_form
from .models import News_post, Advanced_user, Comment_model, Pictures_for_news

# CBV
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView


def index(request):
    all_news = News_post.objects.all()
    context = {
    'all_news': all_news,
    }
    return render(request, 'main/index.html', context)


def news_information(slug):
    # обновляем счетчик просмотра
    news = News_post.objects.get(slug=slug)
    News_post.objects.filter(slug=slug).update(news_views_count=news.news_views_count + 1)

    # достаем всю необходимую для страницы информацию
    news = News_post.objects.get(slug=slug)
    form = Comment_form()
    user_comments = Comment_model.objects.filter(article=news.pk)
    comment_count = len(user_comments)
    pictures = Pictures_for_news.objects.filter(parent_news=news.pk)

    # пересчитываю количество комментариев на странице
    news.news_comments_count = comment_count
    news.save()



    context = {
        'news': news,
        'form': form,
        'user_comments': user_comments,
        'pictures': pictures,
    }
    return context


def news_details(request, slug):
    if request.method == 'GET':
        context = news_information(slug)
        return render(request, 'main/pagenews.html', context)
    else:
        form = Comment_form(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_nickname = Advanced_user.objects.get(pk=request.user.pk)
            comment.article = get_object_or_404(News_post, slug=slug)
            comment.save()

        context = news_information(slug)
        return render(request, 'main/pagenews.html', context)


#class ArticleDetail(DetailView):
    #model = Advanced_user

    #def get_queryset(self):
        #qs = super(ArticleDetail, self).get_queryset()
        #if not self.request.user.is_superuser:
        #    qs = qs.filter(is_published=True)
        #return qs


def register_user(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:

                login(request, user)
                return redirect('main:index')

        return redirect('main:index')
    else:
        form = UserForm()
        return render(request, 'main/registration_form.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main: index')
                #return render(request, 'main/index.html')
            else:
                return render(request, 'main/login.html', {'message': 'U Hawe been disabled'})
        else:
            return render(request, 'main/login.html', {'message': 'Invalid login'})
    return render(request, 'main/login.html')


def logout_user(request):
    logout(request)
    return redirect('main:index')
