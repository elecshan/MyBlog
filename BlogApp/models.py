from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    auth = models.CharField(max_length=20)
    date = models.DateTimeField()
    num_share = models.IntegerField()
    num_comment = models.IntegerField()
    # tags = models.ManyToManyField('Tag')
    picture = models.ImageField(upload_to='static/img')
    article = models.TextField()

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    blog_id = models.IntegerField()
    username = models.CharField(max_length=20)
    comment = models.TextField()

    def __unicode__(self):
        return self.blog_id

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tag
