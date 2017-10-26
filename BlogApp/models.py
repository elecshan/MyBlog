from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    auth = models.CharField(max_length=20)
    date = models.DateTimeField()
    num_share = models.IntegerField()
    num_comment = models.IntegerField()
    # tags = models.ManyToManyField('Tag')
    picture = models.ImageField(upload_to='topicImg/blogs')
    # bodyPicture = models.ImageField(upload_to='static/img/blog')
    article = UEditorField(u'Context',width=900, height=400, toolbars="full", imagePath="images/blogs/", filePath="files/blogs/",
                           upload_settings={"imageMaxSize": 1024000}, settings={},command=None,event_handler=None,blank=True)
    # article = models.TextField()

    def __str__(self):
        return self.title

    def introduction(self):
        return self.article[:180]

class Learn(models.Model):
    title = models.CharField(max_length=50)
    auth = models.CharField(max_length=20)
    date = models.DateTimeField()
    num_share = models.IntegerField()
    num_comment = models.IntegerField()
    # tags = models.ManyToManyField('Tag')
    picture = models.ImageField(upload_to='topicImg/learns')
    # bodyPicture = models.ImageField(upload_to='static/img/learn')
    article = UEditorField(u'Context', width=900, height=400, toolbars="full", imagePath="images/learns/", filePath="files/learns/",
                           upload_settings={"imageMaxSize": 1024000}, settings={}, command=None, event_handler=None, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_id = models.IntegerField()
    username = models.CharField(max_length=20)
    comment = models.TextField()

    def __str__(self):
        return self.blog_id

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag
