from django.contrib import admin
from BlogApp.models import Blog, Comment, Tag, Learn

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'auth', 'date')

admin.site.register(Blog, ArticleAdmin)
admin.site.register(Learn, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
