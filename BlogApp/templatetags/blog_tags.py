from django import template
from BlogApp.models import Article, Category, Tag
from django.db.models.aggregates import Count


register = template.Library()


@register.simple_tag
def get_latest_articles(num=5):
    return Article.objects.all().filter(status='p').order_by('-create_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_article=Count('article')).filter(num_article__gt=0).order_by('name')


@register.simple_tag
def get_tags():
    return Tag.objects.all()

