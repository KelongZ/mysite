from django.db import models

# Create your models here.
class ConfigSrc(models.Model):
    name = models.CharField('简称', max_length=255)
    type = models.CharField('数据源类型', max_length=255)
    src_url = models.CharField('数据库名称', max_length=255)
    host = models.CharField('主机名', max_length=255)
    port = models.IntegerField('端口号')
    user = models.CharField('用户名', max_length=255)
    pwd = models.CharField('密码', max_length=255)
    charset = models.CharField('字符集', max_length=255)
    remark = models.CharField('备注', max_length=255)

    class Meta:
        verbose_name = '数据源管理'
        verbose_name_plural = '数据源管理'

    def __str__(self):
        return self.name

class ConfigData(models.Model):
    sys_name = models.CharField('简称', max_length=255)
    name = models.ForeignKey(ConfigSrc, max_length=255, on_delete=models.CASCADE, verbose_name='数据源名称')
    fetch_method = models.CharField('查询方法', max_length=255)
    table_name = models.CharField('表名', max_length=255)
    primary_key = models.CharField('主键', max_length=255)
    remark = models.CharField('备注', max_length=255)

    class Meta:
        verbose_name = '数据集管理（测试返回数据用）'
        verbose_name_plural = '数据集管理（测试返回数据用）'

    def __str__(self):
        return self.sys_name

class SystemProduct(models.Model):
    configsrc = models.ForeignKey(ConfigSrc, max_length=255, on_delete=models.CASCADE, verbose_name='数据源名称')
    table = models.CharField('表名', max_length=255)
    title = models.CharField('标题', max_length=255)
    top_level = models.CharField('第一层级', max_length=255)
    second_level = models.CharField('第二层级', max_length=255, blank=True)
    third_level = models.CharField('第三层级', max_length=255, blank=True)
    fourth_level = models.CharField('第四层级', max_length=255, blank=True)
    note = models.TextField('摘要')
    if_open = models.IntegerField(choices=[(0, '否'), (1, '是'), ], default=0, verbose_name='是否对外')
    createtime = models.DateTimeField('发布时间', blank=True, null=True)
    updatetime = models.DateTimeField('修改时间', auto_now=True , blank=True, null=True)

    class Meta:
        verbose_name = 'sys_product'
        verbose_name_plural = 'sys_product'

    def __str__(self):
        return self.title

class DataProduct(models.Model):
    table = models.CharField('表名', max_length=255, blank=True)
    title = models.CharField('标题', max_length=255, blank=True)
    x_axis = models.CharField('x_axis', max_length=255)
    x_cn = models.CharField('x_cn', max_length=255)
    y_axis = models.CharField('y_axis', max_length=255)
    y_cn = models.CharField('y_cn', max_length=255)
    z_axis = models.CharField('z_axis', max_length=255, blank=True)
    z_cn = models.CharField('z_cn', max_length=255, blank=True)
    unit = models.CharField('单位', max_length=255)
    chart_type = models.CharField('图表类型', max_length=255)
    time_cyc = models.CharField('周期', max_length=255)
    chart_descrip = models.TextField('图表描述')
    stat_way = models.TextField('统计方式')
    note = models.TextField('备注')
    read_field = models.TextField('执行语句', max_length=255)
    status = models.IntegerField(choices=[(0, '停用'), (1, '可用'), ], default=1, verbose_name='可用状态')
    createtime = models.DateTimeField('发布时间', blank=True, null=True)
    updatetime = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'data_product'
        verbose_name_plural = 'data_product'

    def __str__(self):
        return self.title

class ConfigMenu(models.Model):
    name = models.CharField('节点名称', max_length=255)
    parentID = models.IntegerField('父ID')
    url = models.CharField('链接', max_length=2000)

    # 定义一个方法
    def parent_node_name(self):
        return ConfigMenu.objects.get(id=self.parentID)

    # 设置方法字段在admin中显示的标题
    parent_node_name.short_description = "父节点名称"

    class Meta:
        verbose_name = '菜单管理'
        verbose_name_plural = '菜单管理'

    def __str__(self):
        return self.name

