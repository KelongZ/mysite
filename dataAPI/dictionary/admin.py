from django.contrib import admin
from .models import ConfigSrc, ConfigData, SystemProduct, DataProduct, ConfigMenu
# Register your models here.
@admin.register(ConfigSrc)
class ConfigSrcAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'src_url','host','port', 'user', 'pwd', 'charset', 'remark')
    list_display_links = ('name',)
    list_filter = ['name','type']
    search_fields = ['name', 'type', 'src_url']

@admin.register(ConfigData)
class ConfigDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'sys_name', 'name', 'fetch_method', 'table_name', 'primary_key', 'remark')
    list_display_links = ('sys_name',)

@admin.register(SystemProduct)
class SystemProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'configsrc', 'table', 'title', 'top_level', 'second_level', 'third_level',
                    'fourth_level', 'note', 'if_open', 'createtime', 'updatetime')
    list_display_links = ('table',)
    list_per_page = 50
    search_fields = ['table', 'title', 'top_level', 'second_level', 'third_level',
                    'fourth_level',]

@admin.register(DataProduct)
class DataProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'title', 'x_axis', 'x_cn', 'y_axis', 'y_cn', 'z_axis', 'z_cn', 'unit', 'chart_type',
                    'time_cyc', 'chart_descrip', 'stat_way', 'note', 'read_field', 'status','createtime', 'updatetime')
    list_display_links = ('table',)
    list_per_page = 50
    search_fields = ['table', 'title', 'chart_type',]

@admin.register(ConfigMenu)
class ConfigMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parentID', 'parent_node_name', 'url')
    list_display_links = ('name',)
    list_per_page = 50
    search_fields = ['name',]

admin.site.site_header = '数据集市后台数据管理'
admin.site.site_title = '数据集市'