from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField('分类', max_length=100)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.name
#
class Tags(models.Model):
    name = models.CharField('标签', max_length=100)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    keywords = models.CharField('文章关键词', max_length=120, blank=True, null=True)
    intro = models.TextField('摘要', max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', default='1')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='标签')
    body = models.TextField('内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', default='')

    views = models.PositiveIntegerField('阅读量', default=0)
    top = models.IntegerField(choices=[(0, '否'), (1, '是'), ], default=0, verbose_name='是否推荐')

    created_time = models.DateTimeField('发布时间')
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    # 定义一个方法
    def riqi(self):
        return self.created_time.strftime("%b %d %Y %H:%M:%S")
    # 设置方法字段在admin中显示的标题
    riqi.short_description = "发布日期"
    # 指定排序依据
    riqi.admin_order_field = 'created_time'

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title