import smtplib
from email.mime.text import MIMEText
from email.header import Header

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from BlogApp.models import  Blog, Learn
from django.template import Template, Context


# Create your views here.

def home(request):
    return render(request, 'home.html')

def life(request):
    # top_four_blogs = []
    blogs = Blog.objects.order_by('date').reverse()[:4]
    context = {}
    origin_key = 'blog'
    i = 1
    # for item in blogs:
    #     top_four_blogs.append(item)
    for item in blogs:
        key = origin_key + str(i)
        temp = {key: item}
        context.update(temp)
        i += 1
    return render(request, 'life.html', context)

def learn(request):
    context = {}
    learnList = []
    origin_key = 'learn'
    articles = Blog.objects.order_by('date').reverse().all()
    totalRecord = 0
    for item in articles:
        totalRecord += 1
    context['totalRecord'] = int(totalRecord)
    pageNum = int(totalRecord / 7 + 1)
    pageList = list(range(1, pageNum + 1))
    context['pageNum'] = pageNum
    context['pageNumList'] = pageList
    if request.GET.get('page') is not None and request.GET.get('page') != 1:
        requestPage = int(request.GET.get('page'))
        start = int((requestPage - 1) * 7)
        end = start + 7
        for item in articles[start:end]:
            if item is not None:
                learnList.append(item)
        if requestPage < pageNum:
            context['nextPage'] = requestPage + 1
        else:
            context['nextPage'] = requestPage
    else:
        context['nextPage'] = 1
        for item in articles[:7]:
            if item is not None:
                learnList.append(item)
    context['learn'] = learnList
    return render(request, 'learn.html', context)

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

def getBlogPage(request):
    id = request.GET['id']
    blog = Blog.objects.get(id=id)
    # print(blog.article)
    return render(request, 'blogPage.html', {'blog': blog})
