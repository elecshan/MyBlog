from django.contrib import admin
from BlogApp.models import Article, Category, Tag

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'body', 'status', 'abstract', 'topped', 'category', 'tags')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
