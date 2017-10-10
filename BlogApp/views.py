from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from BlogApp.models import  Blog
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
    return render(request, 'learn.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def getBlogPage(request):
    id = request.GET['id']
    blog = Blog.objects.get(id=id)
    return render(request, 'blogPage.html', {'blog': blog})
