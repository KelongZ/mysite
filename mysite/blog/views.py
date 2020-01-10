from django.shortcuts import render
from django.http import HttpResponse
from blog import models

# Create your views here.
def hello(request):
    return HttpResponse('Hello,world')

def test(request):
    return render(request, 'test.html')

def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    context = {
        'blog_index': blog_index,
    }
    return render(request, 'index.html', context)

def year_archive(request,year,month):
    return  HttpResponse('year:%d month:%d' % (year,month))

def article_detail(request,year,month,slug):
    return HttpResponse('year:%s month:%s slug:%s' % (year,month,slug))

# def orm(request):
#     # 增加一篇文章
#     models.Article.objects.create(title='增加标题一', category_id=3, body='增加内容一', user_id=1)
#     return HttpResponse('orm')