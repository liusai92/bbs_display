# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['title']}),
                 ('Author and Date', {'fields':['author','timestamp']}),
                 (None, {'fields':['body']})]
    inlines = [CommentInline]
    list_display = ('article_id', 'title','author','timestamp')
    list_display_links = ('article_id', 'title')
    list_filter = ['timestamp']
    list_per_page = 20
    search_fields = ['title']
admin.site.register(Article, ArticleAdmin)
