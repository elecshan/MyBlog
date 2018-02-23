from django.db import models
from django.utils.html import strip_tags
import markdown

# Create your models here.


class Category(models.Model):
    name = models.CharField('类名', max_length=32)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('类名', max_length=32)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (('d', 'Draft'), ('p', 'Published'))
    title = models.CharField('标题', max_length=64)
    body = models.TextField('正文')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=150, blank=True, null=True, help_text='可选，如若为空将摘取正文的前54个字符')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞量', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.abstract:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.abstract = strip_tags(md.convert(self.body))[:150]
        super(Article, self).save(*args, **kwargs)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-last_modified_time']


class Comment(models.Model):
    name = models.CharField('名字', max_length=128)
    email = models.EmailField('邮箱', max_length=256)
    url = models.URLField('链接', blank=True)
    comment = models.TextField('评论正文')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    article = models.ForeignKey('Article', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.comment[:20]
