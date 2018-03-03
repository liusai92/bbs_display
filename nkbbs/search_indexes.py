# encoding: utf-8

from nkbbs.models import Article, Comment

from haystack import indexes


# More typical usage involves creating a subclassed `SearchIndex`. This will
# provide more control over how data is indexed, generally resulting in better
# search.
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # We can pull data straight out of the model via `model_attr`.
    author = indexes.CharField(model_attr='author')
    pub_date = indexes.DateField(model_attr='timestamp')

    def get_model(self):
        return Article
