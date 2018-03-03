# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment
from django.db import connection
# Create your views here.

def getLatest(request):
    nb = Article.objects.count()
    articles = Article.objects.raw('select article_id, title, author, timestamp from nkbbs_article where article_id between %s and %s', [nb-20, nb])
    return render(request, 'nkbbs/index.html', {'articles':articles})

def getArticle(request, aid):
    with connection.cursor() as cur:
        connection.connection.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
        cur.execute('select article_id, title, author, body, timestamp from nkbbs_article where article_id={};'.format(aid))
        article_raw = cur.fetchone()
        if article_raw is None:
            raise Http404('Article {} does not exist'.format(aid))
        cur.execute('select author, timestamp, comment_text, article_id_id from nkbbs_comment where article_id_id={};'.format(aid))
        comments_raw = cur.fetchall()
        #construct model from raw_data, include string encoding/decoding
        #Article
        article = Article(article_id=article_raw[0], title=article_raw[1], author=article_raw[2], body=article_raw[3], timestamp=article_raw[4])
        #Comment
        comments = []
        for ele in comments_raw:
            co = Comment(author=ele[0], timestamp=ele[1], comment_text=ele[2], article_id_id=ele[3])
            comments.append(co)
        return render(request, 'nkbbs/detail.html',{'article':article, 'comments':comments})

def getArticleResult(request):
    article_id = request.POST.get('article_id')
    return HttpResponseRedirect('/nkbbs/detail/{}'.format(article_id))

def getArticleList(request):
    article_list = Article.objects.values('article_id','title','author','timestamp')
    paginator = Paginator(article_list, 50) #show 50 items per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page( paginator.num_pages)

    return render(request, 'nkbbs/list.html', {'articles': articles })
