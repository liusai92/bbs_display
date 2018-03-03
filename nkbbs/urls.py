from django.conf.urls import url

from . import views

app_name = 'nkbbs'
urlpatterns = [
    url(r'^$', views.getLatest, name='index'),
    url(r'^detail/(?P<aid>[0-9]+)/$', views.getArticle, name='article_detail'),
    url(r'^result/$', views.getArticleResult, name='result'),
    url(r'^list/$', views.getArticleList, name='article_list'),
]
