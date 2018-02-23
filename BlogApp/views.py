import smtplib
from email.mime.text import MIMEText
from email.header import Header


import markdown
import markdown2
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models.aggregates import Count
from .commentForm import CommentForm
from BlogApp.models import Article, Category


# Create your views here.
class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'
    paginate_by = 3

    def get_queryset(self):
        article_list = Article.objects.all().filter(status='p').order_by('-create_time')
        return article_list

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        left = {}
        right = {}
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            # 如果用户请求的是第一页的数据，那么当前页左边的不需要数据，因此 left=[]（已默认为空）。
            # 此时只要获取当前页右边的连续页码号，
            # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 right = [2, 3]。
            # 注意这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
            right = page_range[page_number:page_number + 2]

            # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
            # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
            if right[-1] < total_pages - 1:
                right_has_more = True

            # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
            # 所以需要显示最后一页的页码号，通过 last 来指示
            if right[-1] < total_pages:
                last = True

        elif page_number == total_pages:
            # 如果用户请求的是最后一页的数据，那么当前页右边就不需要数据，因此 right=[]（已默认为空），
            # 此时只要获取当前页左边的连续页码号。
            # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 left = [2, 3]
            # 这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

            # 如果最左边的页码号比第 2 页页码号还大，
            # 说明最左边的页码号和第 1 页的页码号之间还有其它页码，因此需要显示省略号，通过 left_has_more 来指示。
            if left[0] > 2:
                left_has_more = True

            # 如果最左边的页码号比第 1 页的页码号大，说明当前页左边的连续页码号中不包含第一页的页码，
            # 所以需要显示第一页的页码号，通过 first 来指示
            if left[0] > 1:
                first = True
        else:
            # 用户请求的既不是最后一页，也不是第 1 页，则需要获取当前页左右两边的连续页码号，
            # 这里只获取了当前页码前后连续两个页码，你可以更改这个数字以获取更多页码。
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]

            # 是否需要显示最后一页和最后一页前的省略号
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

            # 是否需要显示第 1 页和第 1 页后的省略号
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data


class TagView(ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
        return article_list

    # def get_context_data(self, **kwargs):
    #     kwargs['tag_list'] = Tag.objects.all().order_by('name')
    #     return super(TagView, self).get_context_data(**kwargs)


class CategoryView(ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['category_id'], status='p')
        return article_list

    # def get_context_data(self, **kwargs):
    #     kwargs['tag_list'] = Category.objects.all().order_by('name')
    #     return super(CategoryView, self).get_context_data(**kwargs)


class ArchiveView(ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        # 月份的filter要注意时区的设置，要将USE_TZ设置为False
        article_list = Article.objects.filter(status='p', create_time__year=year, create_time__month=month)
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'])
        return article_list

    # def get_context_data(self, **kwargs):
    #     kwargs['tag_list'] = Tag.objects.all().order_by('name')
    #     return super(ArchiveView, self).get_context_data(**kwargs)


# def index(request):
#     article_list = Article.objects.all().filter(status='p').order_by('-create_time')
#     return render(request, 'index.html', context={'article_list': article_list})


def categories(request):
    article_dic = {}
    category_list = Category.objects.annotate(num_article=Count('article')).filter(num_article__gt=0).order_by('-name')
    for category in category_list:
        print(category.name)
        article_dic[category] = Article.objects.all().filter(category=category.id, status='p')
    context = {'article_dic': article_dic}
    return render(request, 'category.html', context=context)


def full_width(request):
    article_list = Article.objects.all().filter(status='p').order_by('-create_time')
    return render(request, 'full-width.html', context={'article_list': article_list})


def article_page(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.increase_views()
    md = markdown.Markdown(extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         TocExtension(slugify=slugify)
                                     ])
    article.body = md.convert(article.body)
    article.toc = md.toc
    form = CommentForm()
    comment_list = article.comment_set.all()
    context = {'article': article,
               'form': form,
               'comment_list': comment_list}
    return render(request, 'single.html', context=context)


def post_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(reverse('article_page', args=[article.id]))
        else:
            comment_list = article.comment_set.all()
            context = {'article': article,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'single.html', context=context)
    return redirect(reverse('views.article_page', article.id))


def contact(request):
    return render(request, 'contact.html')


def processcontact(request):
    if request.method == 'POST':
        mail_host = 'smtp.qq.com'
        mail_user = '512499349'
        mail_passwd = 'xgsg7163994'
        receiver = ['xgs951230@163.com']
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['message']
        message = MIMEText(text, 'plain', 'utf-8')
        message['From'] = Header(name, 'utf-8')
        message['To'] = Header('shan', 'utf-8')
        subject = '博客来信'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)
            smtpObj.login(mail_user, mail_passwd)
            smtpObj.sendmail(email, receiver, message.as_string())
            success = True
        except smtplib.SMTPException:
            sucess = False
        return render(request, 'processcontact.html')


def about(request):
    return render(request, 'about.html')

