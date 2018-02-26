from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^categories$', views.categories, name='category_page'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^archive/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.ArchiveView.as_view(), name='archive'),
    url(r'^category/(?P<category_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^comment/article/(?P<article_id>[0-9]+)$', views.post_comment, name='comment'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
