# Generated by Django 3.0.2 on 2020-02-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigSrc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='简称')),
                ('type', models.CharField(max_length=255, verbose_name='数据源类型')),
                ('src_url', models.CharField(max_length=255, verbose_name='数据库名称')),
                ('host', models.CharField(max_length=255, verbose_name='主机名')),
                ('port', models.CharField(max_length=255, verbose_name='端口号')),
                ('user', models.CharField(max_length=255, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=255, verbose_name='密码')),
                ('charset', models.CharField(max_length=255, verbose_name='字符集')),
                ('remark', models.CharField(max_length=255, verbose_name='备注')),
            ],
            options={
                'verbose_name': '数据源管理',
                'verbose_name_plural': '数据源管理',
            },
        ),
    ]