from django.shortcuts import render
from django.http import HttpResponse
from blog import models
import time
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

def orm(request):
    # 增加一篇文章
    # 第一种方法：
    #models.Article.objects.create(title='增加标题一', category_id=3, body='增加内容一', user_id=1, created_time='2020-1-13 3:27:00')
    # 第二种方法：添加数据，实例化表类，在实例化里传参为字段和值
    # obj = models.Article(title='增加标题二', category_id=4, body='增加内容二', user_id=1, created_time='2020-1-13 3:55:00')
    # # 写入数据库
    # obj.save()
    # # 第三种方法：将要写入的数据组合成字典，键为字段值为数据
    # dic = {'title': '增加标题三', 'category_id': '4', 'body': '增加内容三', 'user_id': '1', 'created_time': '2020-1-13 4:27:00'}
    # # 添加到数据库，注意字典变量名称一定要加**
    # models.Article.objects.create(**dic)

    #删除id=6的文章（数据）
    # title = models.Article.objects.filter(id=5).delete()

    # 把标题'增加标题二'，修改成'我被修改了'。将指定条件的数据更新，支持 **kwargs，支持字典。
    #title = models.Article.objects.filter(title='增加标题二').update(title='我被修改了')
    all_article = models.Article.objects.all()
    print(all_article)
    return HttpResponse('orm')