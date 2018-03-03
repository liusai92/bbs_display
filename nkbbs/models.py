# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=15)
    timestamp = models.DateTimeField('date publised')
    body = models.TextField()

    def __str__(self):
        return self.title.encode('utf-8','ignore') 

    def get_absolute_url(self):
        return "detail/%i/" %self.article_id

@python_2_unicode_compatible
class Comment(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, to_field='article_id')
    author = models.CharField(max_length=35)
    timestamp = models.DateTimeField()
    comment_text = models.TextField()
    def __str__(self):
        return str(self.article_id_id)
